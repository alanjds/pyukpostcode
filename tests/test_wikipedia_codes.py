# coding: utf-8
from __future__ import unicode_literals

from ukpostcode import validate


def test_validation_section():
    """
    Validation:

    The format is as follows, where A signifies a letter and 9 a digit:

    Format	Coverage	Example
    AA9A 9AA	WC postcode area; EC1–EC4, NW1W, SE1P, SW1	EC1A 1BB
    A9A 9AA	E1W, N1C, N1P	W1A 0AX
    A9 9AA	B, E, G, L, M, N, S, W	M1 1AE
    A99 9AA	B33 8TH
    AA9 9AA	All other postcodes	CR2 6XH
    AA99 9AA	DN55 1PT
    """
    assert validate('EC1A 1BB') is True
    assert validate('W1A 0AX') is True
    assert validate('M1 1AE') is True
    assert validate('B33 8TH') is True
    assert validate('CR2 6XH') is True
    assert validate('DN55 1PT') is True


def test_specialcases_section():
    """
    Special cases

    Despite this they adopted the UK format postcodes, Guernsey in 1993 using GY,
    the Isle of Man the same year using IM, and Jersey in 1994 using JE.[28]

    AI-2640	Anguilla[29]

    ASCN 1ZZ
    STHL 1ZZ
    TDCU 1ZZ	Saint Helena, Ascension and Tristan da Cunha:
    Ascension Island
    Saint Helena
    Tristan da Cunha[30]
    BBND 1ZZ	British Indian Ocean Territory
    BIQQ 1ZZ	British Antarctic Territory
    FIQQ 1ZZ	Falkland Islands
    GX11 1AA	Gibraltar
    PCRN 1ZZ	Pitcairn Islands
    SIQQ 1ZZ	South Georgia and the South Sandwich Islands
    TKCA 1ZZ	Turks and Caicos Islands[31]
    """
    assert validate('GY1 1BB') is True
    assert validate('IM1 0AX') is True
    assert validate('JE1 1AE') is True

    # assert validate('AI-2640') is True     # Does not validate @ postcodes.io.

    assert validate('ASCN 1ZZ') is True
    assert validate('STHL 1ZZ') is True
    assert validate('TDCU 1ZZ') is True
    assert validate('BBND 1ZZ') is True
    assert validate('BIQQ 1ZZ') is True
    assert validate('FIQQ 1ZZ') is True
    assert validate('GX11 1ZZ') is True
    assert validate('PCRN 1ZZ') is True
    assert validate('SIQQ 1ZZ') is True
    assert validate('TKCA 1ZZ') is True


def test_specialpostcodes_section():
    """
    Special postcodes
    """
    assert validate('BS98 1TL')     #	TV Licensing[44]
    assert validate('BX1 1LT')      #	Lloyds Bank formerly known as Lloyds TSB Bank[45] – non-geographic address
    assert validate('BX2 1LB')      #	Bank of Scotland (part of Lloyds Banking Group)[46] – non-geographic address
    assert validate('BX3 2BB')      #	Barclays Bank[47] – non-geographic address
    assert validate('BX4 7SB')      #	TSB Bank
    assert validate('BX5 5AT')      #	VAT Central Unit of HM Revenue and Customs[48]
    assert validate('CF10 1BH')     #	Lloyds Banking Group (formerly Black Horse Finance)
    assert validate('CF99 1NA')     #	National Assembly for Wales
    assert validate('CV4 8UW')      #	University of Warwick
    assert validate('DE99 3GG')     #	Egg Banking
    assert validate('DE55 4SW')     #	Slimming World
    assert validate('DH98 1BT')     #	British Telecom
    assert validate('DH99 1NS')     #	National Savings certificates administration
    assert validate('E14 5HQ')      #	HSBC headquarters
    assert validate('E16 1XL')      #	ExCeL London[49]
    assert validate('E20 2AQ')      #	Olympic Aquatics Centre
    assert validate('E20 2BB')      #	Olympic Basketball Arena
    assert validate('E20 2ST')      #	Olympic Stadium
    assert validate('E20 3BS')      #	Olympic Broadcast Centre
    assert validate('E20 3EL')      #	Olympic Velodrome
    assert validate('E20 3ET')      #	Olympic Eton Manor Tennis Courts
    assert validate('E20 3HB')      #	Olympic Handball Arena
    assert validate('E20 3HY')      #	Olympic Hockey Stadium
    assert validate('E98 1SN')      #	The Sun newspaper
    assert validate('E98 1ST')      #	The Sunday Times newspaper
    assert validate('E98 1TT')      #	The Times newspaper
    assert validate('EC2N 2DB')     #	Deutsche Bank
    assert validate('EC4Y 0HQ')     #	Royal Mail Group Ltd headquarters
    assert validate('EH12 1HQ')     #	Royal Bank of Scotland headquarters
    assert validate('EH99 1SP')     #	Scottish Parliament[50]
    assert validate('G58 1SB')      #	National Savings Bank (58 ~= SB)
    assert validate('GIR 0AA')      #	Girobank (now Santander Corporate Banking)
    assert validate('IV21 2LR')     #	Two Lochs Radio
    assert validate('L30 4GB')      #	Girobank (alternative geographic postcode)
    assert validate('LS98 1FD')     #	First Direct bank
    assert validate('N1 9GU')       #	The Guardian newspaper
    assert validate('N81 1ER')      #	Electoral Reform Services[40][51]
    assert validate('NE1 4ST')      #	St James' Park Stadium, Newcastle United
    assert validate('NG80 1EH')     #	Experian Embankment House
    assert validate('NG80 1LH')     #	Experian Lambert House
    assert validate('NG80 1RH')     #	Experian Riverleen House
    assert validate('NG80 1TH')     #	Experian Talbot House
    assert validate('PH1 5RB')      #	Royal Bank of Scotland Perth Chief Office
    assert validate('PH1 2SJ')      #	St Johnstone Football Club
    assert validate('S2 4SU')       #	Sheffield United Football Club
    assert validate('S6 1SW')       #	Sheffield Wednesday Football Club
    assert validate('S14 7UP')      #	The World Snooker Championships at the Crucible Theatre
    assert validate('SA99 1AA')     #	Driver and Vehicle Licensing Agency
    assert validate('SE1 8UJ')      #	Union Jack Club
    assert validate('SM6 0HB')      #	Homebase Limited
    assert validate('SN38 1NW')     #	Nationwide Building Society
    assert validate('SW1A 0AA')     #	House of Commons
    assert validate('SW1A 0PW')     #	House of Lords (Palace of Westminster; see above for House of Commons)
    assert validate('SW1A 1AA')     #	Buckingham Palace (the Monarch)
    assert validate('SW1A 2AA')     #	10 Downing Street (the Prime Minister)
    assert validate('SW1H 0TL')     #	Transport for London (Windsor House, 50 Victoria Street)
    assert validate('SW1P 3EU')     #	European Commission and European Parliament office (European Union)
    assert validate('SW1W 0DT')     #	The Daily Telegraph newspaper
    assert validate('TW8 9GS')      #	GlaxoSmithKline
    assert validate('W1A 1AA')      #	BBC Broadcasting House
    assert validate('W1D 4FA')      #	Betgenius, the former address of The Football Association
    assert validate('W1N 4DJ')      #	BBC Radio 1 (disc jockey)


def test_pseudopostcodes_section():
    """
    ZZ99 - Pseudo Postcodes

    ZZ99 3CZ = England (not otherwise stated)
    ZZ99 3VZ = No fixed abode
    ZZ99 3WZ = Address not known
    ZZ99 2WZ = Northern Ireland (not otherwise stated)
    ZZ99 1WZ = Scotland (not otherwise stated)
    ZZ99 3GZ = Wales (not otherwise stated)
    ZZ99 NNN = normally resident overseas (where NNN is the country code listed in the NHS postcode directory)
    """
    assert validate('ZZ99 3CZ') is True
    assert validate('ZZ99 3VZ') is True
    assert validate('ZZ99 3WZ') is True
    assert validate('ZZ99 2WZ') is True
    assert validate('ZZ99 1WZ') is True
    assert validate('ZZ99 3GZ') is True
    assert validate('ZZ99 BRL') is True


def test_address_formats():
    assert validate('M2 5BQ') is True       # AN NAA
    assert validate('M34 4AB') is True      # ANN NAA
    assert validate('CR0 2YR') is True      # AAN NAA
    assert validate('DN16 9AA') is True     # AANN NAA
    assert validate('W1A 4ZZ') is True      # ANA NAA
    assert validate('EC1A 1HQ ') is True    # AANA NA
