from Series import Series

strangerThings = Series("Stranger Things", "Accion", 4.5, 3, 5)
lucifer = Series("Lucifer", "Comedia", 3, 4, 3)
breakingBad = Series("Breaking Bad", "Ficcion", 4, 9, 64)
bettyLaFea = Series("Betty La Fea", "Romance", 2.5, 6, 10)
bobEsponja = Series("Bob Esponja", "Cartoon", 5, 4, 8)
sandMan = Series("Sand Man", "Comedia", 2.5, 6, 2)

series = [strangerThings, lucifer, breakingBad, bettyLaFea, bobEsponja, sandMan]
nombreSeries = [strangerThings.__getNombre__(), lucifer.__getNombre__(), breakingBad.__getNombre__(), bettyLaFea.__getNombre__(), bobEsponja.__getNombre__(), sandMan.__getNombre__()]
generoSeries = [strangerThings.__getGenero__(), lucifer.__getGenero__(), breakingBad.__getGenero__(), bettyLaFea.__getGenero__(), bobEsponja.__getGenero__(), sandMan.__getGenero__()]
valoracionSeries = [strangerThings.__getValoracion__(), lucifer.__getValoracion__(), breakingBad.__getValoracion__(), bettyLaFea.__getValoracion__(), bobEsponja.__getValoracion__(), sandMan.__getValoracion__()]
tempSeries = [strangerThings.__getCantTemp__(), lucifer.__getCantTemp__(), breakingBad.__getCantTemp__(), bettyLaFea.__getCantTemp__(), bobEsponja.__getCantTemp__(), sandMan.__getCantTemp__()]
tempCap = [strangerThings.__getCantCap__(), lucifer.__getCantCap__(), breakingBad.__getCantCap__(), bettyLaFea.__getCantCap__(), bobEsponja.__getCantCap__(), sandMan.__getCantCap__()]