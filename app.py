import streamlit as st
import joblib
import pandas as pd

# Load the trained model
try:
    car_price_model = joblib.load('./car_price_model.pkl')  # Adjust path if necessary
    st.info("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {str(e)}")

# Company to Model mapping
company_to_models = {
   'Ambassador': [
        'CLASSIC 1500 DSL AC', 'Classic 2000 Dsz', 'Grand 1800 ISZ MPFI PW CL'
    ],
    'Audi': [
        'A4 1.8 TFSI', 'A4 2.0 TDI', 'A4 2.0 TDI 177 Bhp Premium Plus', 'A4 3.0 TDI Quattro',
        'A4 30 TFSI Technology', 'A4 35 TDI Premium', 'A4 35 TDI Premium Plus', 'A4 New 2.0 TDI Multitronic',
        'A5 Sportback', 'A6 2.0 TDI Design Edition', 'A6 2.0 TDI Premium Plus', 'A6 2.7 TDI',
        'A6 2.8 FSI', 'A8 4.2 TDI', 'A8 L 3.0 TDI quattro', 'Q3 2.0 TDI Quattro Premium Plus', 
        'Q3 35 TDI Quattro Technology', 'Q5 2.0 TDI', 'Q5 2.0 TFSI Quattro', 'Q5 2.0 TFSI Quattro Premium Plus',
        'Q5 3.0 TDI Quattro Technology', 'Q7 35 TDI Quattro Premium', 'RS7 2015-2019 Sportback Performance'
    ],
    'BMW': [
        '3 Series 320d Luxury Line', '3 Series 320d Sport', '3 Series 320d Sport Line', 
        '3 Series GT Luxury Line', '5 Series 520d Luxury Line', '5 Series 525d Sedan', '5 Series 530i',
        '7 Series 730Ld', '7 Series Signature 730Ld', 'X1 sDrive 20d Exclusive', 'X1 sDrive 20d xLine', 
        'X1 sDrive20d', 'X1 sDrive20d M Sport', 'X5 xDrive 30d xLine'
    ],
    'Chevrolet': [
        'Aveo 1.4', 'Aveo 1.4 CNG', 'Aveo 1.4 LS', 'Aveo 1.4 LT BSIV', 'Aveo 1.6 LT', 'Aveo 1.6 LT with ABS', 
        'Aveo U-VA 1.2', 'Aveo U-VA 1.2 LS', 'Aveo U-VA 1.2 LT', 'Aveo U-VA 1.2 LT WO ABS Airbag',
        'Beat Diesel', 'Beat Diesel LS', 'Beat Diesel LT', 'Beat Diesel LT Option', 'Beat Diesel PS',
        'Beat LS', 'Beat LT', 'Beat LT LPG', 'Beat LT Option', 'Beat PS', 'Captiva 2.0L VCDi', 
        'Captiva LT', 'Cruze LT', 'Cruze LTZ', 'Cruze LTZ AT', 'Enjoy 1.3 TCDi LS 8', 'Enjoy TCDi LS 8 Seater', 
        'Enjoy TCDi LT 7 Seater', 'Enjoy TCDi LT 8 Seater', 'Enjoy TCDi LTZ 7 Seater', 'Optra 1.6', 
        'Optra 1.6 LS', 'Optra Magnum 2.0 LS', 'Optra Magnum 2.0 LS BSIII', 'Optra Magnum 2.0 LT',
        'Sail 1.2 Base', 'Sail 1.2 LT ABS', 'Sail 1.3 LS', 'Sail Hatchback 1.2 LS', 'Sail Hatchback 1.3 TCDi', 
        'Sail Hatchback 1.3 TCDi LT ABS', 'Sail Hatchback LS ABS', 'Sail Hatchback LT ABS', 'Sail LS ABS',
        'Spark 1.0', 'Spark 1.0 LS', 'Spark 1.0 LT', 'Spark 1.0 LT BS3', 'Spark 1.0 LT Option Pack w/ Airbag', 
        'Spark 1.0 PS', 'Tavera LS B3 7 Seats BSII', 'Tavera LT L1 7 Seats BSIII', 'Tavera Neo 2 LS B4 7 Str BSIII',
        'Tavera Neo 2 LT L 9 Str', 'Tavera Neo 3 10 Seats BSIV', 'Tavera Neo 3 9 Str BSIII', 'Tavera Neo 3 LS 7 C BSIII',
        'Tavera Neo 3 LT 9 Seats BSIII', 'Tavera Neo 3 Max 9 Str BSIII', 'Tavera Neo LS B3 - 7(C) seats BSIII'
    ],
    'Daewoo': ['Matiz SD'],
    'Datsun': [
        'GO A', 'GO Plus A', 'GO Plus A Option Petrol', 'GO Plus Remix Limited Edition', 'GO Plus T',
        'GO Plus T BSIV', 'GO Plus T Option', 'GO Plus T Option BSIV', 'GO Plus T Option Petrol', 'GO T BSIV', 
        'GO T Option BSIV', 'GO T Petrol', 'RediGO 1.0 S', 'RediGO 1.0 T Option', 'RediGO AMT 1.0 S', 'RediGO S', 
        'RediGO SV 1.0', 'RediGO T Option', 'redi-GO AMT 1.0 T Option'
    ],
    'Fiat': [
        '500 Lounge', 'Avventura MULTIJET Emotion', 'Avventura Urban Cross 1.3 Multijet Emotion', 
        'Grande Punto 1.3 Dynamic (Diesel)', 'Grande Punto Active (Diesel)', 'Grande Punto EVO 1.3 Active', 
        'Grande Punto EVO 1.3 Dynamic', 'Grande Punto EVO 90HP 1.3 Sport', 'Grande Punto Emotion 90Hp', 
        'Linea 1.3 Emotion', 'Linea 1.3 Multijet Emotion', 'Linea Active (Diesel)', 'Linea Classic 1.3 Multijet',
        'Linea Dynamic', 'Linea Emotion', 'Linea Emotion (Diesel)', 'Linea T Jet Emotion', 'Linea T Jet Plus', 
        'Palio 1.2 Sport', 'Palio D 1.9 EL PS', 'Punto 1.2 Active', 'Punto 1.3 Active', 'Punto 1.3 Emotion', 
        'Punto 1.4 Emotion', 'Punto EVO 1.3 Dynamic', 'Punto EVO 1.3 Emotion'
    ],
    'Force': ['One EX'],
    'Ford': [
        'Aspire Titanium BSIV', 'Aspire Titanium Diesel BSIV', 'Aspire Titanium Plus BSIV', 
        'Aspire Titanium Plus Diesel BSIV', 'Classic 1.4 Duratorq LXI', 'Classic 1.6 Duratec LXI', 
        'EcoSport 1.5 Diesel Ambiente BSIV', 'EcoSport 1.5 Diesel Titanium BSIV', 'EcoSport 1.5 Diesel Titanium Plus BSIV', 
        'EcoSport 1.5 Diesel Trend BSIV', 'EcoSport 1.5 Diesel Trend Plus BSIV', 'EcoSport 1.5 Petrol Titanium BSIV', 
        'EcoSport 1.5 Petrol Titanium Plus AT BSIV', 'EcoSport 1.5 TDCi Titanium BSIV', 'EcoSport 1.5 TDCi Titanium Plus BE BSIV', 
        'Fiesta 1.4 Duratec ZXI', 'Fiesta 1.4 SXi TDCi', 'Fiesta 1.4 SXi TDCi ABS', 'Fiesta 1.4 ZXi Duratec', 
        'Fiesta 1.4 ZXi Leather', 'Fiesta 1.4 ZXi TDCi ABS', 'Fiesta 1.5 TDCi Ambiente', 'Fiesta 1.5 TDCi Titanium',
        'Fiesta 1.6 Duratec EXI Ltd', 'Fiesta 1.6 Duratec S', 'Fiesta 1.6 ZXi Duratec', 'Fiesta 1.6 ZXi Leather',
        'Fiesta Classic 1.4 Duratorq CLXI', 'Fiesta Classic 1.4 SXI Duratorq', 'Fiesta Classic 1.6 Duratec CLXI', 
        'Fiesta Diesel Style', 'Fiesta Diesel Trend', 'Fiesta Petrol Trend', 'Fiesta Titanium 1.5 TDCi', 'Figo 1.2P Ambiente MT',
        'Figo 1.2P Titanium MT', 'Figo 1.2P Titanium Plus MT', 'Figo 1.5 Sports Edition MT', 'Figo 1.5D Ambiente ABS MT',
        'Figo 1.5D Titanium MT', 'Figo 1.5D Titanium Opt MT', 'Figo 1.5D Trend MT', 'Figo 1.5P Titanium AT', 'Figo Aspire 1.5 TDCi Trend',
        'Figo Aspire 1.5 Ti-VCT Titanium', 'Figo Aspire Facelift', 'Figo Aspire Titanium Plus Diesel', 'Figo Diesel Celebration Edition',
        'Figo Diesel EXI', 'Figo Diesel LXI', 'Figo Diesel Titanium', 'Figo Diesel ZXI', 'Figo Petrol EXI', 'Figo Petrol LXI',
        'Figo Petrol Titanium', 'Figo Petrol ZXI', 'Figo Titanium', 'Figo Titanium Diesel BSIV', 'Figo Trend', 'Freestyle Titanium',
        'Freestyle Titanium Diesel', 'Freestyle Titanium Diesel BSIV', 'Freestyle Titanium Plus', 'Freestyle Titanium Plus Diesel',
        'Freestyle Titanium Plus Diesel BSIV', 'Freestyle Trend Petrol BSIV', 'Fusion 1.6 Duratec Petrol', 'Ikon 1.3 Flair',
        'Ikon 1.3L Rocam Flair', 'Ikon 1.4 TDCi DuraTorq', 'Ikon 1.4 ZXi', 'Ikon 1.6 ZXI NXt', 'Ikon 1.8 D'
    ],
    'Honda': [
        'Accord 2.4 AT', 'Accord 2.4 MT', 'Accord VTi-L (MT)', 'Amaze E i-DTEC', 'Amaze E i-Dtech',
        'Amaze E i-VTEC', 'Amaze E i-Vtech', 'Amaze EX i-Dtech', 'Amaze S AT i-Vtech', 'Amaze S CVT Petrol',
        'Amaze S Diesel', 'Amaze S Petrol BSIV', 'Amaze S i-DTEC', 'Amaze S i-Dtech', 'Amaze S i-VTEC', 
        'Amaze S i-Vtech', 'Amaze SX i-VTEC', 'Amaze V CVT Petrol BSIV', 'Amaze V Diesel BSIV', 'Amaze VX AT i-Vtech',
        'Amaze VX Diesel BSIV', 'Amaze VX O iDTEC', 'Amaze VX Petrol BSIV', 'Amaze VX i-DTEC', 'Amaze VX i-VTEC',
        'BR-V i-DTEC VX MT', 'BR-V i-VTEC S MT', 'BR-V i-VTEC VX MT', 'BRV i-DTEC V MT', 'BRV i-VTEC V MT',
        'Brio 1.2 E MT', 'Brio 1.2 S MT', 'Brio 1.2 S Option MT', 'Brio 1.2 VX MT', 'Brio E MT', 'Brio Exclusive Edition',
        'Brio S MT', 'Brio S Option AT', 'Brio V MT', 'Brio VX', 'CR-V Diesel 4WD', 'City 1.3 DX', 'City 1.3 EXI', 
        'City 1.5 E MT', 'City 1.5 EXI', 'City 1.5 EXI S', 'City 1.5 GXI', 'City 1.5 S MT', 'City 1.5 V AT', 
        'City 1.5 V AT Exclusive', 'City 1.5 V Elegance', 'City 1.5 V MT', 'City Corporate Edition', 'City E',
        'City Edge Edition Diesel SV', 'City S', 'City V AT', 'City V MT', 'City VTEC', 'City VX CVT', 'City VX MT',
        'City i DTEC E', 'City i DTEC S', 'City i DTEC SV', 'City i DTEC V', 'City i DTEC VX', 'City i DTec SV',
        'City i DTec V', 'City i VTEC S', 'City i VTEC SV', 'City i VTEC V', 'City i VTEC VX', 'City i-DTEC SV', 
        'City i-DTEC V', 'City i-DTEC VX', 'City i-DTEC ZX', 'City i-VTEC CVT VX'
    ],
    'Hyundai': [
        'Accent CRDi', 'Accent Executive', 'Accent Executive CNG', 'Accent GLE', 'Accent GLE 1', 'Accent GLE CNG',
        'Accent GLS', 'Accent GLS 1.6 ABS', 'Accent GLX', 'Creta 1.4 CRDi Base', 'Creta 1.4 CRDi S', 'Creta 1.4 CRDi S Plus',
        'Creta 1.4 E Plus', 'Creta 1.4 EX Diesel', 'Creta 1.6 CRDi AT SX Plus', 'Creta 1.6 CRDi SX', 'Creta 1.6 CRDi SX Option',
        'Creta 1.6 CRDi SX Plus', 'Creta 1.6 E Plus', 'Creta 1.6 Gamma SX Plus', 'Creta 1.6 SX', 'Creta 1.6 SX Automatic',
        'Creta 1.6 SX Automatic Diesel', 'Creta 1.6 SX Option', 'Creta 1.6 VTVT AT SX Plus', 'Creta 1.6 VTVT S', 
        'EON 1.0 Era Plus', 'EON 1.0 Kappa Magna Plus', 'EON D Lite', 'EON D Lite Plus', 'EON Era', 'EON Era Plus',
        'EON Era Plus Option', 'EON Era Plus Sports Edition', 'EON LPG Magna Plus', 'EON Magna', 'EON Magna Optional',
        'EON Magna Plus', 'EON Magna Plus Option', 'EON Sportz', 'Elantra 2.0 SX AT', 'Elantra CRDi (Leather Option)',
        'Elantra CRDi S', 'Elantra CRDi SX', 'Elantra SX', 'Elite i20 Asta Option BSIV', 'Elite i20 Asta Option CVT BSIV',
        'Elite i20 Diesel Asta Option', 'Elite i20 Diesel Era', 'Elite i20 Magna Plus BSIV', 'Elite i20 Magna Plus Diesel',
        'Elite i20 Petrol Asta Option', 'Elite i20 Petrol Magna Exective', 'Elite i20 Sportz Plus BSIV', 'Elite i20 Sportz Plus CVT BSIV',
        'Elite i20 Sportz Plus Dual Tone BSIV', 'Elite i20 Getz 1.3 GLS', 'Elite i20 Getz 1.3 GVS', 'Getz 1.5 CRDi GVS',
        'Getz GL', 'Getz GLE', 'Getz GLS', 'Getz GLS ABS', 'Getz GLX', 'Grand i10 1.2 CRDi Asta', 'Grand i10 1.2 CRDi Magna',
        'Grand i10 1.2 CRDi Sportz Option', 'Grand i10 1.2 Kappa Asta', 'Grand i10 1.2 Kappa Era', 'Grand i10 1.2 Kappa Magna AT',
        'Grand i10 1.2 Kappa Magna BSIV', 'Grand i10 1.2 Kappa Sportz AT', 'Grand i10 1.2 Kappa Sportz BSIV', 'Grand i10 1.2 Kappa Sportz Dual Tone',
        'Grand i10 1.2 Kappa Sportz Option', 'Grand i10 AT Asta', 'Grand i10 Asta', 'Grand i10 Asta Option', 'Grand i10 Asta Option AT',
        'Grand i10 CRDi Asta', 'Grand i10 CRDi Asta Option', 'Grand i10 CRDi Magna', 'Grand i10 CRDi Sportz', 'Grand i10 Magna',
        'Grand i10 Magna AT', 'Grand i10 Nios AMT Magna', 'Grand i10 Nios Magna CRDi', 'Grand i10 Nios Sportz', 'Grand i10 Sportz',
        'Santa Fe 4WD AT', 'Santa Fe 4X4', 'Santro AT', 'Santro AT CNG', 'Santro Asta', 'Santro Era', 'Santro GLS I - Euro I',
        'Santro GLS I - Euro II', 'Santro GS', 'Santro LE', 'Santro LE zipPlus', 'Santro LP zipPlus', 'Santro LS zipPlus',
        'Santro Magna AMT BSIV', 'Santro Magna BSIV', 'Santro Magna CNG BSIV', 'Santro Sportz AMT', 'Santro Sportz BSIV',
        'Santro Xing GL', 'Santro Xing GL PLUS CNG', 'Santro Xing GL Plus', 'Santro Xing GL Plus LPG', 'Santro Xing GLS',
        'Santro Xing GLS Audio LPG', 'Santro Xing GLS CNG', 'Santro Xing XG', 'Santro Xing XG AT', 'Santro Xing XG eRLX Euro III',
        'Santro Xing XK', 'Santro Xing XK (Non-AC)', 'Santro Xing XK eRLX EuroIII', 'Santro Xing XL AT eRLX Euro III',
        'Santro Xing XL eRLX Euro III', 'Santro Xing XO', 'Santro Xing XS', 'Santro Xing XS eRLX Euro III', 'Sonata 2.4L AT',
        'Sonata AT Leather', 'Sonata CRDi M/T', 'Tucson 2.0 e-VGT 2WD AT GL', 'Tucson 2.0 e-VGT 2WD MT', 'Tucson CRDi',
        'Venue SX Opt Diesel', 'Venue SX Opt Turbo BSIV'
    ],
    'Hyundai': [
        'Verna 1.4 CRDi', 'Verna 1.4 EX', 'Verna 1.4 VTVT', 'Verna 1.6 CRDI', 'Verna 1.6 CRDI SX Option', 'Verna 1.6 CRDi AT SX',
        'Verna 1.6 CRDi SX', 'Verna 1.6 SX', 'Verna 1.6 SX CRDi (O)', 'Verna 1.6 SX VTVT', 'Verna 1.6 SX VTVT (O)', 
        'Verna 1.6 SX VTVT AT', 'Verna 1.6 VTVT', 'Verna 1.6 VTVT AT S Option', 'Verna 1.6 VTVT S', 'Verna 1.6 VTVT SX',
        'Verna 1.6 Xi ABS', 'Verna 1.6 i ABS', 'Verna CRDi', 'Verna CRDi 1.6 AT EX', 'Verna CRDi 1.6 AT SX Option',
        'Verna CRDi 1.6 EX', 'Verna CRDi 1.6 SX', 'Verna CRDi 1.6 SX Option', 'Verna CRDi ABS', 'Verna CRDi SX', 
        'Verna CRDi SX ABS', 'Verna SX', 'Verna SX AT Diesel', 'Verna SX CRDi AT', 'Verna SX Diesel', 'Verna Transform CRDi VGT ABS',
        'Verna Transform CRDi VGT SX ABS', 'Verna Transform SX VTVT', 'Verna Transform VTVT', 'Verna VTVT 1.6 AT SX Option',
        'Verna VTVT 1.6 SX', 'Verna XXi (Petrol)', 'Verna i (Petrol)', 'Xcent 1.1 CRDi Base', 'Xcent 1.1 CRDi S', 'Xcent 1.1 CRDi SX',
        'Xcent 1.1 CRDi SX Option', 'Xcent 1.2 CRDi E', 'Xcent 1.2 CRDi S', 'Xcent 1.2 CRDi SX', 'Xcent 1.2 Kappa Base',
        'Xcent 1.2 Kappa S', 'Xcent 1.2 Kappa SX', 'Xcent 1.2 VTVT E Plus', 'Xcent 1.2 VTVT S', 'Xcent 1.2 VTVT S AT',
        'Xcent 1.2 VTVT S Plus', 'Xcent 1.2 VTVT S Plus', 'i10 Asta AT', 'i10 Era', 'i10 Era 1.1', 'i10 Era 1.1 iTech SE', 
        'i10 Magna', 'i10 Magna 1.1', 'i10 Magna 1.1 iTech SE', 'i10 Magna 1.1L', 'i10 Magna 1.2', 'i10 Magna 1.2 iTech SE',
        'i10 Magna LPG', 'i10 Sportz', 'i10 Sportz 1.1L', 'i10 Sportz 1.2', 'i10 Sportz 1.2 AT', 'i10 Sportz AT',
        'i20 1.2 Asta', 'i20 1.2 Asta Dual Tone', 'i20 1.2 Asta Option', 'i20 1.2 Era', 'i20 1.2 Magna', 'i20 1.2 Magna Executive',
        'i20 1.2 Sportz', 'i20 1.2 Spotz', 'i20 1.4 Asta Option', 'i20 1.4 CRDi Asta', 'i20 1.4 CRDi Era', 'i20 1.4 CRDi Magna',
        'i20 1.4 CRDi Sportz', 'i20 1.4 Magna ABS', 'i20 1.4 Magna Executive', 'i20 1.4 Sportz', 'i20 2015-2017 Magna 1.2',
        'i20 2015-2017 Sportz Option 1.4 CRDi', 'i20 Active 1.2 S', 'i20 Active 1.2 SX', 'i20 Active 1.4 SX', 'i20 Active 1.4 SX with AVN',
        'i20 Active S Diesel', 'i20 Active S Petrol', 'i20 Active SX Petrol', 'i20 Asta', 'i20 Asta (o)', 'i20 Asta (o) 1.4 CRDi (Diesel)',
        'i20 Asta 1.2', 'i20 Asta 1.4 CRDi', 'i20 Asta 1.4 CRDi (Diesel)', 'i20 Asta Option 1.2', 'i20 Asta Option 1.4 CRDi',
        'i20 Magna', 'i20 Magna 1.2', 'i20 Magna 1.4 CRDi', 'i20 Magna 1.4 CRDi (Diesel)', 'i20 Magna Optional 1.2', 
        'i20 Magna Optional 1.4 CRDi', 'i20 Sportz 1.2', 'i20 Sportz 1.4 CRDi', 'i20 Sportz Option 1.2', 'i20 Sportz Petrol'
    ],
    'Isuzu': [
        'D-Max V-Cross Standard'
    ],
    'Jaguar': [
        'XF 2.2 Litre Luxury', 'XF 3.0 Litre S Premium Luxury', 'XF 5.0 Litre V8 Petrol', 
        'XJ 5.0 L V8 Supercharged'
    ],
    'Jeep': [
        'Compass 1.4 Sport Plus BSIV', 'Compass 2.0 Longitude Option BSIV'
    ],
    'Kia': [
        'Seltos HTK Plus AT D'
    ],
    'Land Rover': [
        'Discovery S 2.0 SD4', 'Discovery Sport SD4 HSE Luxury', 'Discovery Sport TD4 HSE 7S', 
        'Range Rover 4.4 Diesel LWB Vogue SE', 'Range Rover Evoque 2.2L Dynamic'
    ],
    'MG': [
        'Hector Sharp Diesel MT BSIV', 'Hector Smart AT'
    ],
    'Mahindra': [
        'Alturas G4 4X2 AT BSIV', 'Bolero 2011-2019 SLE', 'Bolero 2011-2019 SLX', 'Bolero 2011-2019 SLX 2WD BSIII',
        'Bolero B4', 'Bolero B6', 'Bolero DI', 'Bolero DI DX 7 Seater', 'Bolero DI DX 8 Seater', 
        'Bolero Power Plus LX', 'Bolero Power Plus Plus AC BSIV PS', 'Bolero Power Plus Plus Non AC BSIV PS',
        'Bolero Power Plus SLE', 'Bolero Power Plus SLX', 'Bolero Power Plus ZLX', 'Bolero SLE', 
        'Bolero SLE BSIII', 'Bolero SLX', 'Bolero SLX 2WD', 'Bolero SLX 2WD BSIII', 'Bolero SLX 4WD BSIII', 
        'Bolero SLX 4WD BSIII', 'Ingenio CRDe', 'Jeep CJ 500 DI', 'Jeep CL 500 MDI', 'Jeep Classic', 
        'Jeep MM 540', 'Jeep MM 550 XDB', 'Jeep MM 775 XDB', 'KUV 100 D75 K2', 'KUV 100 D75 K4 Plus 5Str', 
        'KUV 100 D75 K6 Plus', 'KUV 100 G80 K2', 'KUV 100 G80 K4 Plus', 'KUV 100 mFALCON D75 K6', 
        'KUV 100 mFALCON G80 K2', 'KUV 100 mFALCON G80 K2 Plus', 'KUV 100 mFALCON G80 K8 5str', 
        'Marazzo M2 8Str', 'Marazzo M4', 'Marazzo M8 8Str', 'NuvoSport N8', 'Quanto C4', 'Quanto C6', 
        'Quanto C8', 'Renault Logan 1.4 GLX Petrol', 'Renault Logan 1.5 DLE Diesel', 'Renault Logan 1.5 DLS', 
        'Renault Logan 1.5 DLX Diesel', 'Renault Logan 1.6 Petrol GLSX', 'Scorpio 1.99 S10', 'Scorpio 1.99 S4', 
        'Scorpio 1.99 S6 Plus', 'Scorpio 2.6 CRDe', 'Scorpio 2.6 CRDe SLE', 'Scorpio 2.6 SLX CRDe', 
        'Scorpio 2.6 SLX Turbo 7 Seater', 'Scorpio 2.6 Turbo 7 Str', 'Scorpio 2.6 Turbo 9 Str', 'Scorpio BSIV', 
        'Scorpio EX', 'Scorpio LX', 'Scorpio LX BSIV', 'Scorpio M2DI', 'Scorpio REV 116', 'Scorpio S10 7 Seater', 
        'Scorpio S11 BSIV', 'Scorpio S2 7 Seater', 'Scorpio S2 9 Seater', 'Scorpio S4 4WD', 'Scorpio S5 BSIV', 
        'Scorpio S6 Plus 7 Seater', 'Scorpio S7 140 BSIV', 'Scorpio S9 BSIV', 'Scorpio SLE BS IV', 
        'Scorpio SLE BSIII', 'Scorpio SLE BSIV', 'Scorpio SLX 2.6 Turbo 8 Str', 'Scorpio VLS 2.2 mHawk', 
        'Scorpio VLS AT 2.2 mHAWK', 'Scorpio VLX 2.2 mHawk Airbag BSIV', 'Scorpio VLX 2WD ABS AT BSIII',
        'Scorpio VLX 2WD AIRBAG BSIV', 'Scorpio VLX 2WD AIRBAG SE BSIV', 'Scorpio VLX 2WD AT BSIV', 
        'Scorpio VLX 2WD BSIII', 'Scorpio VLX 2WD BSIV', 'Scorpio VLX AT 2WD BSIII', 'Supro VX 8 Str', 
        'TUV 300 Plus P4', 'TUV 300 T10', 'TUV 300 T10 Dual Tone', 'TUV 300 T4', 'TUV 300 T4 Plus', 
        'TUV 300 T6 Plus', 'TUV 300 T8', 'TUV 300 T8 AMT', 'TUV 300 mHAWK100 T8', 'Thar 4X2', 'Thar 4X4', 
        'Thar CRDe', 'Thar CRDe ABS', 'Thar CRDe AC', 'Thar DI 4X2', 'Thar DI 4X4 PS', 'Verito 1.5 D2 BSIII', 
        'Verito 1.5 D2 BSIV', 'Verito 1.5 D4 BSIV', 'Verito 1.5 D6 BSIII', 'Verito Vibe 1.5 dCi D4', 'Verito Vibe 1.5 dCi D6', 
        'XUV300 W8 Option', 'XUV300 W8 Option Diesel BSIV', 'XUV500 AT W10 1.99 mHawk', 'XUV500 AT W10 AWD', 
        'XUV500 AT W10 FWD', 'XUV500 AT W6 2WD', 'XUV500 AT W8 FWD', 'XUV500 W10 1.99 mHawk', 'XUV500 W10 2WD',
        'XUV500 W10 AWD', 'XUV500 W11 AT BSIV', 'XUV500 W11 Option AT AWD', 'XUV500 W11 Option AWD', 'XUV500 W5 BSIV', 
        'XUV500 W6 1.99 mHawk', 'XUV500 W6 2WD', 'XUV500 W7', 'XUV500 W7 AT BSIV', 'XUV500 W7 BSIV', 'XUV500 W8 2WD',
        'XUV500 W8 4WD', 'Xylo Celebration Edition BSIV', 'Xylo D2', 'Xylo D2 BS IV', 'Xylo D2 BSIV', 'Xylo D2 Maxx',
        'Xylo D4', 'Xylo D4 BSIV', 'Xylo E4', 'Xylo E4 8S', 'Xylo E4 ABS BS IV', 'Xylo E4 BS III', 'Xylo E6', 
        'Xylo E8', 'Xylo E8 ABS Airbag BSIV', 'Xylo E9', 'Xylo H4', 'Xylo H4 ABS', 'Xylo H8 ABS with Airbags'
    ],
    'Maruti': [
        '800 AC', '800 AC BSII', '800 AC BSIII', '800 AC Uniq', '800 DUO AC LPG', '800 DX', '800 EX', '800 Std', 
        '800 Std BSII', '800 Std BSIII', '800 Std MPFi', 'A-Star AT VXI', 'A-Star Lxi', 'A-Star Vxi', 'Alto 800 Base', 
        'Alto 800 CNG LXI', 'Alto 800 CNG LXI Optional', 'Alto 800 LX', 'Alto 800 LXI', 'Alto 800 LXI Airbag', 'Alto 800 LXI CNG', 
        'Alto 800 LXI Opt BSIV', 'Alto 800 LXI Optional', 'Alto 800 Std Optional', 'Alto 800 VXI', 'Alto Green LXi (CNG)', 
        'Alto K10 2010-2014 VXI', 'Alto K10 LX', 'Alto K10 LXI', 'Alto K10 LXI CNG', 'Alto K10 LXI CNG Optional', 'Alto K10 VXI',
        'Alto K10 VXI AGS', 'Alto K10 VXI AGS Optional', 'Alto K10 VXI Airbag', 'Alto K10 VXI Optional', 'Alto LX', 'Alto LX BSIII', 
        'Alto LXI', 'Alto LXi', 'Alto LXi BSII', 'Alto LXi BSIII', 'Alto STD', 'Alto VXi', 'Baleno Alpha', 'Baleno Alpha 1.2',
        'Baleno Alpha 1.3', 'Baleno Alpha CVT', 'Baleno Delta 1.2', 'Baleno Delta 1.3', 'Baleno Delta Automatic', 'Baleno RS 1.0 Petrol',
        'Baleno Sigma 1.2', 'Baleno Vxi', 'Baleno Zeta', 'Baleno Zeta 1.2', 'Baleno Zeta 1.3', 'Baleno Zeta Automatic', 
        'Celerio Green VXI', 'Celerio LXI MT BSIV', 'Celerio VDi', 'Celerio VXI', 'Celerio VXI AMT BSIV', 'Celerio VXI AT',
        'Celerio VXI Optional', 'Celerio X ZXI BSIV', 'Celerio ZDi', 'Celerio ZXI', 'Celerio ZXI AMT BSIV', 'Celerio ZXI AT', 
        'Celerio ZXI MT BSIV', 'Celerio ZXI Optional AMT BSIV', 'Ciaz 1.3 Delta', 'Ciaz 1.4 AT Zeta', 'Ciaz 1.4 Alpha',
        'Ciaz 1.4 Delta', 'Ciaz 1.4 Zeta', 'Ciaz S 1.3', 'Ciaz Sigma BSIV', 'Ciaz VDI SHVS', 'Ciaz VDi', 'Ciaz VDi Option SHVS',
        'Ciaz VDi Plus', 'Ciaz VDi Plus SHVS', 'Ciaz ZDi', 'Ciaz ZDi Plus', 'Ciaz ZDi Plus SHVS', 'Ciaz ZDi SHVS', 
        'Ciaz ZXi', 'Ciaz ZXi Plus', 'Eeco 5 STR With AC Plus HTR CNG', 'Eeco 5 Seater AC BSIV', 'Eeco 5 Seater Standard BSIV',
        'Eeco 7 Seater Standard BSIV', 'Eeco CNG 5 Seater AC BSIV', 'Eeco Smiles 5 Seater AC', 'Ertiga 1.5 VDI', 'Ertiga BSIV VXI AT',
        'Ertiga BSIV ZXI', 'Ertiga SHVS LDI', 'Ertiga SHVS LDI Option', 'Ertiga SHVS VDI', 'Ertiga SHVS ZDI', 'Ertiga SHVS ZDI Plus',
        'Ertiga VDI', 'Ertiga VDI Limited Edition', 'Ertiga VXI', 'Ertiga VXI ABS', 'Ertiga VXI CNG', 'Ertiga VXI Petrol',
        'Ertiga ZDI', 'Ertiga ZDI Plus', 'Ertiga ZXI', 'Ertiga ZXI AT Petrol', 'Esteem AX', 'Esteem Lxi', 'Esteem Lxi - BSIII',
        'Esteem VX', 'Esteem Vxi', 'Esteem Vxi - BSIII', 'Estilo LXI', 'Grand Vitara MT', 'Gypsy E MG410W ST', 'Gypsy King HT BSIV',
        'Gypsy King Hard Top', 'Gypsy King Hard Top Ambulance BSIV', 'Ignis 1.2 AMT Alpha BSIV', 'Ignis 1.2 AMT Delta BSIV',
        'Ignis 1.2 Alpha BSIV', 'Ignis 1.2 Delta BSIV', 'Ignis 1.2 Sigma BSIV', 'Ignis 1.2 Zeta BSIV', 'Ignis 1.3 Delta',
        'Omni 5 Str STD', 'Omni 5 Str STD LPG', 'Omni 8 Seater BSII', 'Omni 8 Seater BSIV', 'Omni BSIII 8-STR W/ IMMOBILISER',
        'Omni CNG', 'Omni E 8 Str STD', 'Omni E MPI STD BS IV', 'Omni LPG CARGO BSIII W IMMOBILISER', 'Omni LPG STD BSIV',
        'Omni MPI STD BSIV', 'Omni Maruti Omni MPI STD BSIII 5-STR W/ IMMOBILISER', 'Ritz LDi', 'Ritz LXI', 'Ritz LXi',
        'Ritz VDI (ABS) BS IV', 'Ritz VDi', 'Ritz VXI', 'Ritz VXi', 'S-Cross Alpha DDiS 200 SH', 'S-Cross Delta DDiS 200 SH',
        'S-Cross Facelift', 'S-Cross Sigma DDiS 200 SH', 'S-Cross Zeta DDiS 200 SH', 'S-Presso VXI Plus', 'SX4 Celebration Diesel',
        'SX4 Celebration Petrol', 'SX4 S Cross DDiS 320 Delta', 'SX4 S Cross DDiS 320 Zeta', 'SX4 VDI', 'SX4 Vxi BSIII', 
        'SX4 Vxi BSIV', 'SX4 ZDI', 'SX4 ZDI Leather', 'SX4 ZXI AT', 'SX4 ZXI MT BSIV', 'SX4 Zxi BSIII', 'SX4 Zxi with Leather BSIII',
        'Swift 1.2 DLX', 'Swift 1.3 DLX', 'Swift 1.3 LXI', 'Swift 1.3 VXI ABS', 'Swift 1.3 VXi', 'Swift AMT VXI', 'Swift DDiS LDI',
        'Swift DDiS VDI', 'Swift Dzire 1.2 Vxi BSIV', 'Swift Dzire AMT VDI', 'Swift Dzire AMT VXI', 'Swift Dzire AMT ZXI',
        'Swift Dzire AMT ZXI Plus BS IV', 'Swift Dzire LDI', 'Swift Dzire LDI Optional', 'Swift Dzire LDIX Limited Edition',
        'Swift Dzire LDi', 'Swift Dzire LXI', 'Swift Dzire LXI Option', 'Swift Dzire LXi', 'Swift Dzire Tour LDI', 'Swift Dzire VDI',
        'Swift Dzire VDI Optional', 'Swift Dzire VDi', 'Swift Dzire VXI', 'Swift Dzire VXI 1.2 BS IV', 'Swift Dzire VXi',
        'Swift Dzire Vdi BSIV', 'Swift Dzire ZDI', 'Swift Dzire ZXI', 'Swift Dzire ZXI 1.2 BS IV', 'Swift Dzire ZXI Plus', 
        'Swift Glam', 'Swift LDI', 'Swift LDI BSIV', 'Swift LDI Optional', 'Swift LXI', 'Swift LXI Option', 'Swift LXi BSIV',
        'Swift Ldi BSIII', 'Swift Ldi BSIV', 'Swift Star VDI', 'Swift VDI', 'Swift VDI BSIV', 'Swift VDI Optional', 'Swift VDi BSIII W/ ABS',
        'Swift VVT VXI', 'Swift VVT ZXI', 'Swift VXI', 'Swift VXI BSIII', 'Swift VXI BSIV', 'Swift VXI Deca', 'Swift VXI Optional',
        'Swift VXI with ABS', 'Swift VXi BSIV', 'Swift Vdi BSIII', 'Swift ZDI', 'Swift ZDI Plus', 'Swift ZDi', 'Swift ZDi BSIV',
        'Swift ZXI Plus'
    ],
    'Toyota': [
        'Camry 2.5 Hybrid', 'Camry Hybrid', 'Camry Hybrid 2.5', 'Camry M/t', 'Corolla AE', 'Corolla Altis 1.8 GL', 
        'Corolla Altis 1.8 J', 'Corolla Altis 1.8 VL AT', 'Corolla Altis 1.8 VL CVT', 'Corolla Altis D-4D J', 'Corolla Altis Diesel D4DG',
        'Corolla Altis Diesel D4DGL', 'Corolla Altis Diesel D4DJ', 'Corolla Altis G', 'Corolla Altis G AT', 'Corolla Altis GL MT',
        'Corolla Executive (HE)', 'Corolla H2', 'Corolla H3', 'Corolla H6', 'Etios 1.4 VXD', 'Etios 1.5 V', 'Etios Cross 1.2L G',
        'Etios Cross 1.4L GD', 'Etios GD', 'Etios GD SP', 'Etios Liva 1.2 G', 'Etios Liva 1.2 V', 'Etios Liva 1.2 VX', 
        'Etios Liva 1.4 VD', 'Etios Liva G', 'Etios Liva GD', 'Etios Liva GD SP', 'Etios Liva VD', 'Etios Liva VX', 
        'Etios V', 'Etios VD', 'Etios VX', 'Etios VXD', 'Fortuner 2.7 2WD AT', 'Fortuner 2.8 2WD AT BSIV', 'Fortuner 2.8 4WD AT BSIV',
        'Fortuner 3.0 Diesel', 'Fortuner 4x2 AT', 'Fortuner 4x2 Manual', 'Fortuner 4x4 MT', 'Innova 2.0 GX 8 STR BSIV', 'Innova 2.0 VX 7 Seater',
        'Innova 2.5 E 8 STR', 'Innova 2.5 E Diesel MS 7-seater', 'Innova 2.5 EV Diesel MS 7 Str BSIII', 'Innova 2.5 EV Diesel PS 7 Seater BSIII',
        'Innova 2.5 G (Diesel) 7 Seater', 'Innova 2.5 G (Diesel) 7 Seater BS IV', 'Innova 2.5 G (Diesel) 8 Seater', 
        'Innova 2.5 G (Diesel) 8 Seater BS IV', 'Innova 2.5 G1 BSIV', 'Innova 2.5 G3', 'Innova 2.5 G4 Diesel 7-seater', 
        'Innova 2.5 G4 Diesel 8-seater', 'Innova 2.5 GX (Diesel) 7 Seater', 'Innova 2.5 GX (Diesel) 7 Seater BS IV', 
        'Innova 2.5 GX (Diesel) 8 Seater', 'Innova 2.5 GX (Diesel) 8 Seater BS IV', 'Innova 2.5 GX 7 STR', 'Innova 2.5 GX 7 STR BSIV', 
        'Innova 2.5 GX 8 STR BSIV', 'Innova 2.5 V Diesel 7-seater', 'Innova 2.5 V Diesel 8-seater', 'Innova 2.5 VX (Diesel) 7 Seater',
        'Innova 2.5 VX (Diesel) 7 Seater BS IV', 'Innova 2.5 VX (Diesel) 8 Seater', 'Innova 2.5 VX (Diesel) 8 Seater BS IV', 
        'Innova 2.5 VX 8 STR', 'Innova 2.5 VX 8 STR BSIV', 'Innova 2.5 Z Diesel 7 Seater BS IV', 'Innova Crysta 2.4 G MT BSIV',
        'Innova Crysta 2.4 GX AT', 'Innova Crysta 2.4 GX MT 8S BSIV', 'Innova Crysta 2.4 VX MT', 'Innova Crysta 2.4 VX MT 8S BSIV',
        'Innova Crysta 2.4 VX MT BSIV', 'Innova Crysta 2.4 ZX MT', 'Innova Crysta 2.5 VX BS IV', 'Innova Crysta 2.8 GX AT BSIV',
        'Innova Crysta 2.8 ZX AT BSIV', 'Qualis FS B3', 'Yaris G'
    ]
}
# Streamlit app interface
st.title("Car Price Predictor")

# User input fields
st.header("Enter Car Details")

# Company Dropdown
company = st.selectbox("Select Company", options=list(company_to_models.keys()))

# Filter Models Based on Selected Company
models = company_to_models[company]

# Search Bar for Model Selection
search_text = st.text_input("Search for car model", "")
filtered_models = [model for model in models if search_text.lower() in model.lower()]

# Dropdown to select model from filtered results
if filtered_models:
    selected_model = st.selectbox("Select Model", options=filtered_models)
else:
    selected_model = st.selectbox("Select Model", options=[])

# Other car details
year = st.number_input("Enter Car Year", min_value=2000, max_value=2025, step=1)
km_driven = st.number_input("Enter Kilometers Driven", min_value=0)

# Dropdowns for categorical features
fuel = st.selectbox("Select Fuel Type", options=['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
transmission = st.selectbox("Select Transmission Type", options=['Manual', 'Automatic'])
seller_type = st.selectbox("Select Seller Type", options=['Dealer', 'Individual', 'Trustmark Dealer'])
owner = st.selectbox("Select Number of Owners", options=['First Owner', 'Second Owner', 'Third Owner', 'Fourth Owner'])

# Predict button
if st.button("Predict"):
    try:
        # Prepare input for prediction
        input_data = pd.DataFrame([[year, km_driven, fuel, transmission, seller_type, owner, company, selected_model]],
                                  columns=['year', 'km_driven', 'fuel', 'transmission', 'seller_type', 'owner', 'company', 'model'])
        prediction = car_price_model.predict(input_data)  # Make prediction
        st.success(f"The estimated selling price is: ₹{round(prediction[0], 2)}")
    except Exception as e:
        st.error(f"Error occurred while making prediction: {str(e)}")
