from django.shortcuts import render

#import numpy as np
# Create your views here.
from django.http import HttpResponse #,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from avarunsite.forms import LoginForm
from avarunsite.views import HomePageView
#@login_required
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
#    return HttpResponseRedirect("https://www.avarun.cn/stocksdemo")
 
class IndexView(HomePageView):
    template_name='modeling/surface3d.html'
    
    import numpy as np
    from bokeh.embed import components 
    from bokeh.models import ColumnDataSource,CustomJS,Slider
    #from bokeh.plotting import output_file, show
    from .surface3d.surface3d import Surface3d
    from bokeh.layouts import column, row
    #output_file("/data/avarun/avarunsite/modeling/templates/modeling/3d.html")   
    x = np.arange(0, 300, 10)
    y = np.arange(0, 300, 10)
    xx, yy = np.meshgrid(x, y)
    xx = xx.ravel()
    yy = yy.ravel()
    
    t=0
    value = np.sin(xx/50 + t/10) * np.cos(yy/50 + t/10) * 50 + 50
    source = ColumnDataSource(data=dict(x=xx,y=yy,z=value,color=value))
    
    #content_filename = "/data/avarun/avarunsite/modeling/surface3d/description.html"
    
    #description = Div(text=open(content_filename).read(),
    #                  render_as_text=False, width=600)
    
    surface = Surface3d(x="x", y="y", z="z", color="color", data_source=source)

    callback = CustomJS(args=dict(source=source), code="""
            var data = source.data;
            var f = cb_obj.value;

            var x = data['x'];
            var y = data['y'];
            var z = data['z'];
            var color = data['color'];
            for (j = 0; j < y.length; j++) {
                    z[j] = Math.sin(x[j]/50 + f/10)*Math.cos(y[j]/50 + f/10) * 50 + 50; 
            };
            source.change.emit();
        """)

    slider = Slider(start=1, end=100, value=0, step=1, title="Phase")
    slider.js_on_change('value', callback)

    p=column(slider,surface)
    #show(p)
    
    script,div = components(p)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['script'] = self.script
        context['div'] = self.div
        return context
    
    

class SimulationView(HomePageView):
    template_name='modeling/simulation.html'
    from bokeh.layouts import column
    from bokeh.models import CustomJS, ColumnDataSource, Slider
    from bokeh.plotting import Figure, output_file, show
    from bokeh.embed import components
    
    x = [x*0.005 for x in range(0, 200)]
    y = x
    
    source = ColumnDataSource(data=dict(x=x, y=y))
    
    plot = Figure(plot_width=400, plot_height=400)
    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
    
    callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var f = cb_obj.value
        x = data['x']
        y = data['y']
        for (i = 0; i < x.length; i++) {
            y[i] = Math.pow(x[i], f)
        }
        source.change.emit();
    """)
    
    slider = Slider(start=0.1, end=4, value=1, step=.1, title="power")
    slider.js_on_change('value', callback)
    
    layout = column(slider, plot)
    
    #show(layout)

    script,div = components(layout)    
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['script'] = self.script
        context['div'] = self.div
        return context



class PredictionView(HomePageView):
    template_name='modeling/simulation.html'

    from bokeh.models import ColumnDataSource, Whisker, BoxSelectTool
    from bokeh.plotting import figure, show
    from bokeh.sampledata.autompg import autompg as df
    from bokeh.layouts import layout, widgetbox
    from bokeh.models.widgets.tables import DataTable, TableColumn
    
    from bokeh.embed import components
    
    colors = ["red", "olive", "darkred", "goldenrod", "skyblue", "orange", "salmon"]
    
    p = figure(plot_width=600, plot_height=300, title="Years vs mpg with Quartile Ranges")
    
    base, lower, upper = [], [], []
    
    
    for i, year in enumerate(list(df.yr.unique())):
        year_mpgs = df[df['yr'] == year]['mpg']
        mpgs_mean = year_mpgs.mean()
        mpgs_std = year_mpgs.std()
        lower.append(mpgs_mean - mpgs_std)
        upper.append(mpgs_mean + mpgs_std)
        base.append(year)
    
    source_error = ColumnDataSource(data=dict(base=base, lower=lower, upper=upper))
    
    p.add_layout(
        Whisker(source=source_error, base="base", upper="upper", lower="lower")
    )
    
    for i, year in enumerate(list(df.yr.unique())):
        y = df[df['yr'] == year]['mpg']
        color = colors[i % len(colors)]
        p.circle(x=year, y=y, color=color)
    
    source = ColumnDataSource(df)
    p1 = figure(plot_width=600, plot_height=300)
    p1.circle(x="mpg",y="cyl",source=source)
    p1.add_tools(BoxSelectTool())
    columns = [
            TableColumn(field="mpg", title="mpg"),
            TableColumn(field="cyl", title="cyl"),
            TableColumn(field="displ", title="displ"),
            TableColumn(field="hp", title="hp"), 
            TableColumn(field="weight", title="weight"),
            TableColumn(field="accel", title="accel"), 
            TableColumn(field="yr", title="yr"),
            TableColumn(field="origin", title="origin"),
            TableColumn(field="name", title="name") 
        ]
    dt=DataTable(source=source,columns=columns)
    
    l=layout([p,p1,widgetbox(dt)])
        
    
    script,div = components(l)    
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['script'] = self.script
        context['div'] = self.div
        return context

   





class GroupSummariesView(HomePageView):
    template_name='modeling/group_summaries.html'

class OthersView(HomePageView):
    template_name='modeling/others.html'


