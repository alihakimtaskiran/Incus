# Incus
## Acoustic FDTD Simulator
Acoustic Simulator for Python


    pip install incus
    
### Tree   
<pre>
|----Continuum(object)----|
|                         |---__init__(grid_size,ds)
|                         |---add(arg)
|                         |---__categorizer()
|                         |---__emo_video_creator()
|                         |---__grid_generator_at_t_0()
|                         |---__update_grid()
|                         |---export_grid()
|                         |---build(verbose=1)
|                         |---__prefix_quantifier(quantity)
|                         |---__convert_to_time(time_in_secs)
|                         |---__create_progress_bar_with_ETA(current_time,current_step,total_steps)
|                         |---impose_grid(c,rho)
|                         |---view_structure(field="c",*args,colorbar=True)
|                         |---view_field(field="P",*args,colorbar=True)
|                         |---__numpy_renderer(*args)
|                         |---Render(time_steps,backend="numpy",observers=None)
|                         |---__Z()
|
|
|
|----DotSource(object)----|
|                         |---__init__(location,presence,amplitude,frequency,phase=0)
|                         |---__repr__()
|                         |---set_dt(dt)
|                         |---inf()
|                         |---dimensionality()
|                         |---location()
|                         |---__call__(t)
|
|
|
|---geo(module)-----------|----PointCloud(object)-------|
                          |                             |---__init__(points,layer=0,c=331.29,rho=1.225,time=None)
                          |
                          |
                          |----Rectangle(PointCloud)----|
                          |                             |---__init__(A,B,layer=0,c=331.29,rho=1.225,time=None)
                          |
                          |
                          |----RectPrism(PointCloud)----|
                          |                             |---__init__(A,B,layer=0,c=331.29,rho=1.225,time=None)
                          |
                          |
                          |----Circle(object)-----------|
                          |
                          |
                          |----Sphere(object)-----------|
                          |                             |---__init__(A,r,layer=0,c=331.29,rho=1.225,time=None)
                          |
                          |
                          |----Cylinder(object)---------|
                                                        |---__init__(A,r,h,layer=0,c=331.29,rho=1.225,time=None)

</pre>
