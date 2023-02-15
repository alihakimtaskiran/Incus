import incus
grid=incus.Continuum((100,100),1)
grid.add(incus.DotSource((50,50), (0,10000), 5, 80))
grid.add(incus.geo.Circle((50,50),20,4,1050,.187))
grid.build()
grid.view_structure("rho")
grid.Render(300)
grid.view_field("P")
