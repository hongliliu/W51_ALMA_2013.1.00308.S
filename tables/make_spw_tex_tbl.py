from astropy.table import Table, Column
from astropy import units as u

tbl = Table.read('spw_table.txt', format='ascii')

frq_range = list(zip(tbl['Ch0(MHz)']*u.MHz, (tbl['Ch0(MHz)'] + tbl['ChanWid(kHz)']/1e3*tbl['#Chans'])*u.MHz))

tbl.add_column(Column(data=u.Quantity([min(x) for x in frq_range], u.GHz), name='Minimum Frequency'))
tbl.add_column(Column(data=u.Quantity([max(x) for x in frq_range], u.GHz), name='Maximum Frequency'))
tbl.rename_column('ChanWid(kHz)', 'Channel Width')
tbl['Channel Width'].unit = u.kHz

tbl = tbl['SpwID', 'Minimum Frequency', 'Maximum Frequency', 'Channel Width']
tbl.write('../cores_and_outflows/spwtable.tex', overwrite=True)
