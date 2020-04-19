# Covid-19 Township- and Facility-Level Datasets for Myanmar

This repo tries to tackle the issue of the lack of consolidated open data for the fight against coronavirus in Myanmar and make the case for releaseing more open data from the government side so that the public decision makers can allocate the resources efficiently and focus on the most needed areas. 

This repo also tries to help web developers, data visualizers, journalists and researchers to build tools that can help the decision-making process more evidence-based and help the community respond in most efficient ways. 

### Who owns the data?

All of these data are publicly available open data produced, digitized or maintained by public offices and non-profit organizations, namely MoHS, DoMS, GAD, TAF, ODMM and MIMU. 

A group of volunteers and a Ananda staff contributed their private time for scrapping, data entry, cleaning and compiling these datasets.

Please note that these data are not perfect and need checking and adding, so we would love to include as much relevant information as possible here. So, we need your help! 

And always refer to the original source.   

We all know that we can make use of much more information, such as list of hospitals with ventilators, which the goverment is likely to hold in any format. So, hey, the Ministry of Health and Sports, please release more relevant information however imperfect they maybe. You can make use of the civic hackers out there to clean them. 

### Data Dictionary  

# `Covid-19 Baseline Township Data.csv`

| data           | description                                   | source                              |
| -------------- | --------------------------------------------- | ----------------------------------- |
| SR\_PCODE      | တိုင်းဒေသကြိး/ပြည်နယ် Place Code              | MIMU                                |
| SR\_NAME       | တိုင်းဒေသကြီး/ပြည်နယ် (အင်္ဂလိပ်)             | MIMU                                |
| SR\_MM\_NAME   | တိုင်းဒေသကြီး/ပြည်နယ် (မြန်မာ)                | MIMU                                |
| TS\_PCODE      | မြို့နယ် Place Code                           | MIMU                                |
| TS\_NAME       | မြို့နယ် (အင်္ဂလိပ်)                          | MIMU                                |
| TS\_MM\_NAME   | မြို့နယ် (မြန်မာ)                             | MIMU                                |
| POP            | စုစုပေါင်းလူဦးရေ                              | Census via ODMM                     |
| Under\_5\_POP  | အသက်ငါးနှစ်အောက်လူဦးရေ                        | Census via ODMM                     |
| Above\_60\_POP | အသက််ခြောက်ဆယ်အထက်လူဦးရေ                      | Census via ODMM                     |
| MEAN\_HH\_Size | ပျမ်းမျှအိမ်ထောင်စုအရွယ်အစား                  | Census via ODMM                     |
| BED            | မြို့နယ်စုစုပေါင်း အစိုးရ ဆေးရုံကုတင်အရေအတွက် | အထွေထွေအုပ်ချုပ်ရေးဦးစီးဌာန         |
| PHYSNB         | မြို့နယ်စုစုပေါင််း ဆရာဝန်အရေအတွက်            | အထွေထွေအုပ်ချုပ်ရေးဦးစီးဌာန via TAF |
| NURSNB         | မြို့နယ်စုစုပေါင််း သူနာပြုအရေအတွက်           | အထွေထွေအုပ်ချုပ်ရေးဦးစီးဌာန via TAF |
| HSNB           | မြို့နယ်စုစုပေါင််း ကျန်းမာရေးမှူးအရေအတွက်    | အထွေထွေအုပ်ချုပ်ရေးဦးစီးဌာန via TAF |

Source URL[1]: https://data.opendevelopmentmekong.net/dataset/68c62eb8-399d-42f4-a786-131bc0460844

Source URL[2]: https://themimu.info

# `Hospitals.csv`

| data           | description                 | source                      | remark                                                                                             |
| -------------- | --------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------- |
| region         | တိုင်းဒေသကြီး/ပြည်နယ်       | ကုသရေးဦးစီးဌာန              |                                                                                                    |
| township       | မြို့နယ်                    |                             | ကုသရေးမှစာရင်းတွင် မြို့နယ်အလိုက်ခွဲမထားသဖြင့် ထွေအုပ်စာရင်းဖြင့် တိုက်ဆိုင်၍ မြို့နယ်ခွဲထားပါသည်။ |
| hospital\_name | ဆေးရုံအမည်                  | ကုသရေးဦးစီးဌာန              |                                                                                                    |
| level          | ဆေးရုံအဆင့်                 |                             | အမည်ကိုကြည့်၍ ထုတ်နုတ်ထားခြင်းဖြစ်သဖြင့် မပြည့်စုံပါ။                                              |
| bed            | ကုတင်အရေအတွက်               | အထွေထွေအုပ်ချုပ်ရေးဦးစီးဌာန | ကုသရေးဦးစီးဌာနမှ ဆေးရုံစာရင်းနှင့် ထွေအုပ်စာရင်းတွင် ကွဲလွဲမှုအချို့ရှိပါသည်။                      |
| lat            | ဆေးရုံတည်နေရာ လတ္တီကျုဒ်    | ကုသရေးဦးစီးဌာန              |                                                                                                    |
| long           | ဆေးရုံတည်နေရာ လောင်ဂျီကျုဒ် | ကုသရေးဦးစီးဌာန              |                                                                                                    |
| coordinates    | ဆေးရုံတည်နေရာ ကိုသြဓိနိတ်   | ကုသရေးဦးစီးဌာန              |

Source URL[1]: http://www.doms.gov.mm/

Source URL[2]: http://www.gad.gov.mm/my/content/%E1%80%92%E1%80%B1%E1%80%9E%E1%80%86%E1%80%AD%E1%80%AF%E1%80%84%E1%80%BA%E1%80%9B%E1%80%AC%E1%80%A1%E1%80%81%E1%80%BB%E1%80%80%E1%80%BA%E1%80%A1%E1%80%9C%E1%80%80%E1%80%BA%E1%80%99%E1%80%BB%E1%80%AC%E1%80%B8

# `MOHS Dashboard Data.csv`

| data      | description                   | source |
| --------- | ----------------------------- | ------ |
| SR        | တိုင်းဒေသကြီး/ပြည်နယ်         | MoHS   |
| Township  | မြို့နယ်                      | MoHS   |
| Hospital  | ဆေးရုံအမည်(အင်္ဂလိပ်)         | MoHS   |
| HosPt     | စောင့်ကြည့်/သံသယ              | MoHS   |
| PUI       | စောင့်ကြည့်လူနာ               | MoHS   |
| Suspected | သံသယလူနာ                      | MoHS   |
| M         | ကျား                          | MoHS   |
| F         | မ                             | MoHS   |
| Child     | ကလေး                          | MoHS   |
| Adult     | လူကြီး                        | MoHS   |
| Lab\_Neg  | ဓာတ်ခွဲအတည်ပြုပိုးမတွေ့လူနာ   | MoHS   |
| Confirmed | ဓာတ်ခွဲအတည်ပြုပိုးတွေ့လူနာ    | MoHS   |
| Pending   | ဓာတ်ခွဲအဖြေစောင့်ဆိုင်းဆဲလူနာ | MoHS   |
| DC        | ဆေးရုံဆင်းခွင့်ရလူနာ          | MoHS   |
| Latitude  | ဆေးရုံတည်နေရာ လတ္တီကျုဒ်      | MoHS   |
| Longitude | ဆေးရုံတည်နေရာ လောင်ဂျီကျုဒ်   | MoHS   |

Source URL: https://doph.maps.arcgis.com/apps/opsdashboard/index.html#/f8fb4ccc3d2d42c7ab0590dbb3fc26b8

# `Hospital Names in English and Burmese.csv`

| data             | description            | source                            | remark                                                                                                            |
| ---------------- | ---------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| hospital-name-en | ဆေးရုံအမည် (အင်္ဂလိပ်) | ကျန်းမာရေးနှင့် အားကစားဝန်ကြီးဌာန | ကျန်းမာရေးဝန်ကြီးဌာန၏ covid-19 dashboard တွင် ဖော်ပြသည့် ဆေးရုံအမည်များဖြစ်ပါသည်။                                 |
| hospital-name    | ဆေးရုံအမည် (မြန်မာ)    | ကုသရေးဦးစီးဌာန                    | ကုသရေး၏ ဆေးရုံစာရင်းတွင် အသုံးပြုသော အမည်များဖြစ်ပါသည်။ အချို့အမည်များ ထပ်နေသဖြင့် ဒေသအမည်ထပ်ဖြည့်၍ ပြင်ထားပါသည်။ |

# `Medical Supplies with Location.csv`
| data              | description                   | source |
| ----------------- | ----------------------------- | ------ |
| Announcement Date | ကြေငြာချက်ထုတ်သည့်ရက်စွဲ      | MoHS   |
| Hospital-original | ဆေးရုံ (မူရင်းကြေငြာချက်)     | MoHS   |
| hospital-name-mm  | ဆေေးရုံအမည် (မြန်မာ)          | MoHS   |
| PPE               | PPE ဝတ်ဆုံ                    | MoHS   |
| Glove             | လက်အိတ်                       | MoHS   |
| N-95              | N-95 နှာခေါင်းစည်း            | MoHS   |
| Surgical Mask     | ခွဲစိတ်ခန်းသုံး နှာခေါင်းစည်း | MoHS   |
| Goggle            | မျက်မှန်                      | MoHS   |
| Shoe Cover        | ဖိနပ်ပိတ်                     | MoHS   |
| Remarks           | မှတ်ချက်                      | MoHS   |
| Ref               | ရင်းမြစ် (လင့်ခ်)             | MoHS   |
| lat               | လတ္တီကျုဒ်                    | DoMS   |
| long              | လောင်ဂျီကျုဒ်                 | DoMS   |

# `Development Partners Assistance.csv`
| data                 | description         |
| -------------------- | ------------------- |
| Organization/Country | အဖွဲဲ့အစည်း/နိုင်ငံ |
| Date                 | ရက်စွဲ              |
| Description          | ထောက်ပံ့မှု         |
| Type                 | အမျိုးအစား          |
| Amount               | ပမာဏ                |
| Remark               | မှတ်ချက်            |
| Source               | ရင်းမြစ်            |


# `Covid-19 Response Contact List.csv`
| data                   | description                     | source                                                   |
| ---------------------- | ------------------------------- | -------------------------------------------------------- |
| Sector                 | လုပ်ကိုင်ဆောင်ရွက်နေသည့် နယ်ပယ် | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| State\_Region          | တိုင်းဒေသကြီး/ပြည်နယ်           | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| SR\_Pcode              | တိုင််းဒေသကြီး/ပြည်နယ် Pcode    | MIMU                                                     |
| Township               | မြို့နယ်                        | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| Tsp\_Pcode             | မြို့နယ်် Pcode                 | MIMU                                                     |
| Name                   | အမည်                            | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| Organization           | အဖွဲ့အစည်း                      | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| Description            | ရာထူး/အကြောင်းအရာ ဖော်ပြချက်    | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| Contact\_Primary       | အဓိက ဆက်သွယ်ရန် ဖုန်း           | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| Contact\_Secondary     | အခြား ဆက်သွယ်ရန် ဖုန်း          | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| Data\_Submission\_Time | အချက်အလက်ဖြည့်သွင်းသည့်ရက်စွဲ   | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |
| Field\_ID              | အချက််အလက် ID                   | ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက် |

Source URL: https://docs.google.com/spreadsheets/d/1UmXfnox_8M11QBIKuReZlKnN1ppI9bWsYc1RLXNM7jg/edit?fbclid=IwAR2Ys5ygfs8qYsenrDwPxwWJ1oIdBQHU00kfthEUxnUcRHvmvKKFalOFcHY#gid=550445115

# `Community Quarantine Facilities Daily Entry.csv`

| data          | description                                                        | source                  | remark                                                                                        |
| ------------- | ------------------------------------------------------------------ | ----------------------- | --------------------------------------------------------------------------------------------- |
| SR\_Pcode     | တိုင်းဒေသကြီး/ပြည်နယ် Pcode                                        | MIMU                    |                                                                                               |
| State\_Region | တိုင််းဒေသကြီး/ပြည်နယ်                                             | ဒေသခံ စေတနာ့ဝန်ထမ်းများ |                                                                                               |
| Tsp\_Pcode    | မြို့နယ် Pcode                                                     | MIMU                    |                                                                                               |
| Township      | မြို့နယ််                                                          | ဒေသခံ စေတနာ့ဝန်ထမ်းများ |                                                                                               |
| Facility      | ဆေးရုံ/နေရာ                                                        | ဒေသခံ စေတနာ့ဝန်ထမ်းများ |                                                                                               |
| Date          | အသွားအလာကန့်သတ်မှု တည်နေရာသို့ စတင်ဝင်ရောက်သည့်ရက်စွဲ (ရက်/လ/နှစ်) | ဒေသခံ စေတနာ့ဝန်ထမ်းများ | အချို့သော မြို့နယ်များအတွက် ဤအရေအတွက်သည် အချက်အလက် စတင်ကောက်ယူသည့်ရက်စွဲဖြစ်နိုင်ချေရှိပါသည်။ |
| Male          | အမျိုးသား                                                          | ဒေသခံ စေတနာ့ဝန်ထမ်းများ |                                                                                               |
| Female        | အမျိုးသမီး                                                         | ဒေသခံ စေတနာ့ဝန်ထမ်းများ |                                                                                               |
| Total         | စုစုပေါင်း                                                         | ဒေသခံ စေတနာ့ဝန်ထမ်းများ |

# `Facility Needs.csv`
| data                | description                             | source                          |
| ------------------- | --------------------------------------- | ------------------------------- |
| SR\_Pcode           | တိုင်းဒေသကြီး/ပြည်နယ် Pcode             | MIMU                            |
| State\_Region       | တိုင််းဒေသကြီး/ပြည်နယ်                  | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Tsp\_Pcode          | မြို့နယ် Pcode                          | MIMU                            |
| Township            | မြို့နယ််                               | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Facility            | ဆေးရုံ/နေရာ                             | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Description         | လိုအပ်သည့် ပစ္စည်းအမည်                  | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Type                | ပမာဏ အမျိုးအစား                         | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Quantity\_Required  | စုစုပေါင်း လိုအပ်သည့် ပမာဏ              | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Quantity\_Secured   | ရှာဖွေစုဆောင်းထားနိုင်သည့် ပမာဏ         | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Quantity\_Issued    | အသုံးပြုခဲ့သည့်/အသုံးပြုဆဲဖြစ်သည့် ပမာဏ | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Quantity\_In\_Store | သိုလှောင်ရုံတွင် သိမ်းဆည်းထားသည့်ပမာဏ   | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |
| Remark              | မှတ်ချက်                                | ကြို့ပင်ကောက် စေတနာ့ဝန်ထမ်းများ |

# `Foreign Returnees.csv`

| data          | description                 | Source |
| ------------- | --------------------------- | ------ |
| SR\_Pcode     | တိုင်းဒေသကြီး/ပြည်နယ် Pcode | MIMU   |
| State\_Region | တိုင််းဒေသကြီး/ပြည်နယ်      |        |
| Tsp\_Pcode    | မြို့နယ် Pcode              | MIMU   |
| Township      | မြို့နယ််                   |        |
| Country       | သွားရောက်ခဲ့သည့် နိုင်ငံ    |        |
| Returnees     | ပြန်လာသူဦးရေ                |

Source URLs:
- [Taungoo](https://web.facebook.com/tuntunwin.tuntunwin.7/posts/1576515205828936)
- [Nattalin](https://web.facebook.com/Covid19-%E1%80%80%E1%80%BC%E1%80%AD%E1%80%AF%E1%80%90%E1%80%84%E1%80%BA%E1%80%80%E1%80%AC%E1%80%80%E1%80%BD%E1%80%9A%E1%80%BA%E1%80%9B%E1%80%94%E1%80%BA-%E1%80%9B%E1%80%94%E1%80%BA%E1%80%95%E1%80%AF%E1%80%B6%E1%80%84%E1%80%BD%E1%80%B1%E1%80%9B%E1%80%BE%E1%80%AC%E1%80%96%E1%80%BD%E1%80%B1%E1%80%9B%E1%80%B1%E1%80%B8%E1%80%A1%E1%80%96%E1%80%BD%E1%80%B2%E1%80%B7-%E1%80%94%E1%80%90%E1%80%BA%E1%80%90%E1%80%9C%E1%80%84%E1%80%BA%E1%80%B8%E1%80%99%E1%80%BC%E1%80%AD%E1%80%AF%E1%80%B7-101535398166720/?__tn__=kCH-R&eid=ARAWmyq4k2x9a8TRPzd7K1mlPkzg4Qjj7cnTEg9TqOXhSzRRqvYWM6bLmGlcMglF4Y50u_UlJZzoRDWF&hc_ref=ARSqXV4HpcNhX-zGXiNBD0i8ReJpoHhtajQX8zG8APnOtvjJ6j9g4qXsSriXAvSnSAo&fref=nf&__xts__[0]=68.ARAAgcL-CN9UtHPkACbGlBzMPLtDYKZuW0jKpF0MwYB9OcWk1uD0AIapGPpuP5sN6_27YWG5OlpnSZWZ1-NTJ7ew556_h7RHfgW-iic6QxIr82CwkP1H1cyYF-T-UZC0JFhnEJ9FgjAvgXG1IihMLS4YIDXR5Dz7isWWsc_6sRC9UkzlmFgeJX9jflgRIkD67ev60rjaj17BPMvg3PPLSfMtxlRziszeGfWiYP9qA6RC0p-Z4d4Ls7PrQr7TVBBLFVkcw0FaCIrd4PIQKAoNqOE-fzIgiOta0UO_7-X6Yy-jWZsGqVZwcg2ffY880nhLLRdzmBiTTdAajSqBKBvl2ZRf)


# `MoHS Dashboard Data Archive`
Archived datasets of MoHS Dashboard Data

### Contributors/Volunteers

* Kyi Toe
* Phyo Ko Ko
* Ye Min Aung
* Thet Paing Myo
* Myat Min Soe
* Aung Htun Lin (The Ananda)
* Nyan Lynn Myint (The Ananda)
* Htin Kyaw Aye (The Ananda) 

### Credits

* Medical Supplies original dataset compiled by Ko Nyein Chan Ko Ko and volunteers
* Development Partners Assistance data extracted from [this Medium post](https://medium.com/@leighmitchell/how-are-partners-supporting-myanmars-covid-19-response-cda866b6c74) by Leigh Mitchell
* Volunteers from [ကိုရိုနာဗိုင်းရပ်စ် ကောလာဟလ တန်ပြန်တားဆီးရေး လူထုကွန်ရက်](https://web.facebook.com/groups/198360681431931/) for contact list dataset
