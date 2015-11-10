"""
Attempt to image the continuum by flagging out lines, splitting, then doing imaging things...
"""

linechannels12m = '3:233.00835218195223~233.0127460973872GHz,3:233.0166517999961~233.02641605651831GHz,3:233.03227461043164~233.04496814391052GHz,3:233.08939551108662~233.10355368304383GHz,3:233.1064829600005~233.11234151391383GHz,3:233.12991717565382~233.13479930391492GHz,3:233.14114607065437~233.14505177326325GHz,3:233.15091032717658~233.18166773522157GHz,3:233.19973160978765~233.20314909957042GHz,3:233.22902437935429~233.23390650761542GHz,3:233.24952931805095~233.2651521284865GHz,3:233.2876099184876~233.29444489805314GHz,3:233.29835060066202~233.3105559213148GHz,3:233.3154380495759~233.32129660348923GHz,3:233.3330137113159~233.3418015421859GHz,3:233.34424260631644~233.359865416752GHz,3:233.37988214262253~233.40136350697142GHz,3:233.40673384805865~233.41600989175475GHz,3:233.4321209150164~233.4682486641486GHz,3:233.46922508980083~233.5087703287158GHz,3:233.52097564936858~233.52488135197746GHz,3:233.53806309828246~233.55661518567467GHz,3:233.566867655023~233.5824904654585GHz,3:233.6000661271985~233.6132478735035GHz,3:233.62350034285183~233.62594140698238GHz,3:233.65084026111404~233.65669881502737GHz,3:233.66597485872347~233.66841592285402GHz,3:233.67378626394122~233.70942580024732GHz,3:233.72846610046565~233.73237180307453GHz,3:233.74360069807508~233.75629423155397GHz,3:233.75873529568452~233.76264099829342GHz,3:233.77924023438118~233.78265772416395GHz,3:233.79632768329506~233.79974517307784GHz,3:233.8036508756867~233.80902121677394GHz,3:233.84466075308003~233.85442500960224GHz,3:233.85881892503724~233.9530440004766GHz,3:233.9623200441727~233.96769038525994GHz,3:234.0599626093949~234.06777401461267GHz,3:234.07558541983042~234.08925537896152GHz,3:234.13075346918095~234.15174662070373GHz,3:234.20593824440203~234.20886752135868GHz,3:234.2313253113598~234.236695652447GHz,3:234.2635473578831~234.27477625288364GHz,3:234.27575267853587~234.2903990633192GHz,3:234.3045572352764~234.31676255592916GHz,3:234.33336179201692~234.33580285614747GHz,3:234.36704847701856~234.38315950028021GHz,3:234.43686291115242~234.44613895484852GHz,3:234.45248572158798~234.4637146165885GHz,3:234.47347887311074~234.49154274767685GHz,3:234.54475794572292~234.5486636483318GHz,3:234.6297069774662~234.64093587246674GHz,3:234.6472826392062~234.65460583159785GHz,3:234.6663229394245~234.66876400355505GHz,3:234.70879745529612~234.71319137073112GHz,3:234.7307670324711~234.73613737355834GHz,3:234.74541341725444~234.75029554551554GHz,3:234.86356092117327~234.87039590073883GHz,7:233.00835218195223~233.0127460973872GHz,7:233.0166517999961~233.02641605651831GHz,7:233.03227461043164~233.04496814391052GHz,7:233.08939551108662~233.10355368304383GHz,7:233.1064829600005~233.11234151391383GHz,7:233.12991717565382~233.13479930391492GHz,7:233.14114607065437~233.14505177326325GHz,7:233.15091032717658~233.18166773522157GHz,7:233.19973160978765~233.20314909957042GHz,7:233.22902437935429~233.23390650761542GHz,7:233.24952931805095~233.2651521284865GHz,7:233.2876099184876~233.29444489805314GHz,7:233.29835060066202~233.3105559213148GHz,7:233.3154380495759~233.32129660348923GHz,7:233.3330137113159~233.3418015421859GHz,7:233.34424260631644~233.359865416752GHz,7:233.37988214262253~233.40136350697142GHz,7:233.40673384805865~233.41600989175475GHz,7:233.4321209150164~233.4682486641486GHz,7:233.46922508980083~233.5087703287158GHz,7:233.52097564936858~233.52488135197746GHz,7:233.53806309828246~233.55661518567467GHz,7:233.566867655023~233.5824904654585GHz,7:233.6000661271985~233.6132478735035GHz,7:233.62350034285183~233.62594140698238GHz,7:233.65084026111404~233.65669881502737GHz,7:233.66597485872347~233.66841592285402GHz,7:233.67378626394122~233.70942580024732GHz,7:233.72846610046565~233.73237180307453GHz,7:233.74360069807508~233.75629423155397GHz,7:233.75873529568452~233.76264099829342GHz,7:233.77924023438118~233.78265772416395GHz,7:233.79632768329506~233.79974517307784GHz,7:233.8036508756867~233.80902121677394GHz,7:233.84466075308003~233.85442500960224GHz,7:233.85881892503724~233.9530440004766GHz,7:233.9623200441727~233.96769038525994GHz,7:234.0599626093949~234.06777401461267GHz,7:234.07558541983042~234.08925537896152GHz,7:234.13075346918095~234.15174662070373GHz,7:234.20593824440203~234.20886752135868GHz,7:234.2313253113598~234.236695652447GHz,7:234.2635473578831~234.27477625288364GHz,7:234.27575267853587~234.2903990633192GHz,7:234.3045572352764~234.31676255592916GHz,7:234.33336179201692~234.33580285614747GHz,7:234.36704847701856~234.38315950028021GHz,7:234.43686291115242~234.44613895484852GHz,7:234.45248572158798~234.4637146165885GHz,7:234.47347887311074~234.49154274767685GHz,7:234.54475794572292~234.5486636483318GHz,7:234.6297069774662~234.64093587246674GHz,7:234.6472826392062~234.65460583159785GHz,7:234.6663229394245~234.66876400355505GHz,7:234.70879745529612~234.71319137073112GHz,7:234.7307670324711~234.73613737355834GHz,7:234.74541341725444~234.75029554551554GHz,7:234.86356092117327~234.87039590073883GHz'


finalvis12m='calibrated_12m.ms'
contvis12m='w51_spw3_continuum_flagged_12m.split'
flagmanager(vis=finalvis12m,mode='save',
            versionname='before_cont_flags')


flagdata(vis=finalvis12m,mode='manual',
         spw=linechannels12m,flagbackup=False)

split(vis=finalvis12m,
      spw='3,7',
      outputvis=contvis12m,
      width=[192,192],
      datacolumn='data')


flagmanager(vis=finalvis12m,mode='restore',
            versionname='before_cont_flags')

linechannels7m = '3:233.00835218195223~233.0127460973872GHz,3:233.0166517999961~233.02641605651831GHz,3:233.03227461043164~233.04496814391052GHz,3:233.08939551108662~233.10355368304383GHz,3:233.1064829600005~233.11234151391383GHz,3:233.12991717565382~233.13479930391492GHz,3:233.14114607065437~233.14505177326325GHz,3:233.15091032717658~233.18166773522157GHz,3:233.19973160978765~233.20314909957042GHz,3:233.22902437935429~233.23390650761542GHz,3:233.24952931805095~233.2651521284865GHz,3:233.2876099184876~233.29444489805314GHz,3:233.29835060066202~233.3105559213148GHz,3:233.3154380495759~233.32129660348923GHz,3:233.3330137113159~233.3418015421859GHz,3:233.34424260631644~233.359865416752GHz,3:233.37988214262253~233.40136350697142GHz,3:233.40673384805865~233.41600989175475GHz,3:233.4321209150164~233.4682486641486GHz,3:233.46922508980083~233.5087703287158GHz,3:233.52097564936858~233.52488135197746GHz,3:233.53806309828246~233.55661518567467GHz,3:233.566867655023~233.5824904654585GHz,3:233.6000661271985~233.6132478735035GHz,3:233.62350034285183~233.62594140698238GHz,3:233.65084026111404~233.65669881502737GHz,3:233.66597485872347~233.66841592285402GHz,3:233.67378626394122~233.70942580024732GHz,3:233.72846610046565~233.73237180307453GHz,3:233.74360069807508~233.75629423155397GHz,3:233.75873529568452~233.76264099829342GHz,3:233.77924023438118~233.78265772416395GHz,3:233.79632768329506~233.79974517307784GHz,3:233.8036508756867~233.80902121677394GHz,3:233.84466075308003~233.85442500960224GHz,3:233.85881892503724~233.9530440004766GHz,3:233.9623200441727~233.96769038525994GHz,3:234.0599626093949~234.06777401461267GHz,3:234.07558541983042~234.08925537896152GHz,3:234.13075346918095~234.15174662070373GHz,3:234.20593824440203~234.20886752135868GHz,3:234.2313253113598~234.236695652447GHz,3:234.2635473578831~234.27477625288364GHz,3:234.27575267853587~234.2903990633192GHz,3:234.3045572352764~234.31676255592916GHz,3:234.33336179201692~234.33580285614747GHz,3:234.36704847701856~234.38315950028021GHz,3:234.43686291115242~234.44613895484852GHz,3:234.45248572158798~234.4637146165885GHz,3:234.47347887311074~234.49154274767685GHz,3:234.54475794572292~234.5486636483318GHz,3:234.6297069774662~234.64093587246674GHz,3:234.6472826392062~234.65460583159785GHz,3:234.6663229394245~234.66876400355505GHz,3:234.70879745529612~234.71319137073112GHz,3:234.7307670324711~234.73613737355834GHz,3:234.74541341725444~234.75029554551554GHz,3:234.86356092117327~234.87039590073883GHz'
finalvis7m='calibrated_7m.ms'
contvis7m='w51_spw3_continuum_flagged_7m.split'
flagmanager(vis=finalvis7m,mode='save',
            versionname='before_cont_flags')

flagdata(vis=finalvis7m,mode='manual',
         spw=linechannels7m,flagbackup=False)

split(vis=finalvis7m,
      spw='3,7',
      outputvis=contvis7m,
      width=[192,192],
      datacolumn='data')


flagmanager(vis=finalvis7m,mode='restore',
            versionname='before_cont_flags')




contimagename = 'w51_spw3_continuum_7m12m'

for ext in ['.flux','.image','.mask','.model','.pbcor','.psf','.residual','.flux.pbcoverage']:
    rmtables(contimagename+ext)

clean(vis=[contvis7m,contvis12m],
      imagename=contimagename,
      field='w51',
      phasecenter='',
      mode='mfs',
      psfmode='clark',
      imsize = [960,960],
      cell= '0.15arcsec',
      weighting = 'natural',
      robust = 2.0,
      niter = 10000,
      threshold = '1.0mJy',
      interactive = False,
      imagermode = 'mosaic',
      usescratch=False,
      )
exportfits(contimagename+".image", contimagename+".image.fits", dropdeg=True, overwrite=True)


contimagename = 'w51_spw3_continuum_r0'

for ext in ['.flux','.image','.mask','.model','.pbcor','.psf','.residual','.flux.pbcoverage']:
    rmtables(contimagename+ext)

clean(vis=[contvis7m,contvis12m],
      imagename=contimagename,
      field='w51',
      phasecenter='',
      mode='mfs',
      psfmode='clark',
      imsize = [2560,2560],
      cell= '0.052arcsec',
      weighting = 'briggs',
      robust = 0.0,
      niter = 10000,
      threshold = '1.0mJy',
      interactive = False,
      imagermode = 'mosaic',
      usescratch=False,
      )
exportfits(contimagename+".image", contimagename+".image.fits", dropdeg=True, overwrite=True)

contimagename = 'w51_spw3_continuum_r0_dirty'

for ext in ['.flux','.image','.mask','.model','.pbcor','.psf','.residual','.flux.pbcoverage']:
    rmtables(contimagename+ext)

clean(vis=[contvis7m,contvis12m],
      imagename=contimagename,
      field='w51',
      phasecenter='',
      mode='mfs',
      psfmode='clark',
      imsize = [2560,2560],
      cell= '0.052arcsec',
      weighting = 'briggs',
      robust = 0.0,
      niter = 0,
      threshold = '1.0mJy',
      interactive = False,
      imagermode = 'mosaic',
      usescratch=False,
      )
exportfits(contimagename+".image", contimagename+".image.fits", dropdeg=True, overwrite=True)

contimagename = 'w51_spw3_continuum_r0_mulstiscale'

for ext in ['.flux','.image','.mask','.model','.pbcor','.psf','.residual','.flux.pbcoverage']:
    rmtables(contimagename+ext)

clean(vis=[contvis7m,contvis12m],
      imagename=contimagename,
      field='w51',
      multiscale=[0,3,6,9,12,15,18],
      phasecenter='',
      mode='mfs',
      psfmode='clark',
      imsize = [2560,2560],
      cell= '0.052arcsec',
      weighting = 'briggs',
      robust = 0.0,
      niter = 10000,
      threshold = '10.0mJy',
      interactive = False,
      imagermode = 'mosaic',
      usescratch=False,
      )
exportfits(contimagename+".image", contimagename+".image.fits", dropdeg=True, overwrite=True)
