import { Component, OnInit } from '@angular/core';
import { StopService } from '../stop.service';
import { DataService } from './data.service';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  constructor(public stop: StopService) { }


  category = 'bras'
  ngOnInit(): void {
    // window.scroll({'top':0}s)

    // this.stop.get_page(this.stop.page_num)
    // this.products_page = this.products.filter((value,index)=>(index<9) && value.type=='leggings')
  }

  next() {
    this.stop.page_num += 1
    this.stop.get_page(this.stop.page_num)
  }
  previous() {
    this.stop.page_num -= 1
    this.stop.get_page(this.stop.page_num)
  }

  star_size = 'a-icon-star-medium a-star-medium-1'
  star_dict = {
    '1': 'a-icon-star-medium a-star-medium-1',
    '2': 'a-icon-star-medium a-star-medium-2',
    '3': 'a-icon-star-medium a-star-medium-3',
    '4': 'a-icon-star-small a-star-small-4',
    '4.5': 'a-icon-star-small a-star-small-4-5',
    '5': 'a-icon-star-small a-star-small-5'
  }
  star_list = ['',
    'a-icon-star-medium a-star-medium-1',
    'a-icon-star-medium a-star-medium-2',
    'a-icon-star-medium a-star-medium-3',
    'a-icon-star-small a-star-small-4',
    'a-icon-star-small a-star-small-5'
  ]


  //Slider settings
  slideConfig = { "slidesToShow": 1, "slidesToScroll": 1, autoplay: true };
  carousel = [
    { img: 'background-image:url("assets/images/leg3.png") !important' },
    { img: 'background-image:url("assets/images/leg2.png") !important;' },
    { img: 'background-image:url("assets/images/leg1.png") !important; ' }
  ]


  boxes = [
    //1
    [
      {
        img: "https://ae01.alicdn.com/kf/Ha1e1500f450749f5914814af50227cfeL/Cloud-Hide-Women-Yoga-Pants-High-Waist-Sports-Sexy-Butt-Fitness-Leggings-Gym-HOT-Girl-Tights.jpg_Q90.jpg_.webp",
        category: "",
        url: ["leggings"],
        see_more: ["leggings", "shorts"]
      },
      {
        img: "https://ae01.alicdn.com/kf/S8f21c755d123433c940a9e65145c4d08k.jpg",
        category: "",
        url: ["shorts"],
        see_more: ["shorts"]
      },
      {
        img: "https://ae01.alicdn.com/kf/S90a9c61e94124848ad8717945936f4c31.jpg",
        category: "Leggings",
        url: ["leggings"],
        see_more: ["leggings"]
      },
      {
        img: "https://ae01.alicdn.com/kf/Hd711df514288427e9659a87f869241845/Women-High-Waist-Out-Pocket-Yoga-Sports-Short-Running-Athletic-Yoga-Shorts-Pants-Gym-Leggings-Sport.jpg_Q90.jpg_.webp",
        category: "Shorts",
        url: ["shorts"],
        see_more: ["shorts"]
      },
    ],
    //2
    [
      {
        img: "https://ae01.alicdn.com/kf/H2573e62f5a6b4a4392ab6ed055a0d20c1/Soutien-gorge-de-Sport-fort-Impact-pour-femmes-haut-Push-Up-Fitness-course-pied-Yoga-gymnastique.jpg_Q90.jpg_.webp",
        category: "",
        url: ["bras"],
        see_more: ["bras", "tank_tops"]

      },
      {
        img: "https://ae01.alicdn.com/kf/S1bbb31dcc27d445f93378de067cf13d4D/SHINBENE-d-bardeur-de-Sport-2-en-1-l-ger-dos-ouvert-Fitness-sensation-nue-pour.jpg_Q90.jpg_.webp",
        category: "",
        url: ["tank_tops"],
        see_more: ["tank_tops"]
      },
      {
        img: "https://ae01.alicdn.com/kf/Hcc3aa7d964cd4cfdb7c92ac1781cc635I/Padded-Unwired-Bra-Push-Up-Sexy-Lingerie-Tops-For-Girls-Gym-Tank-Top-Yoga-Sport-Bras.jpg_640x640.jpg",
        category: "Bras",
        url: ["bras"],
        see_more: ["bras"]
      },
      {
        img: "https://ae01.alicdn.com/kf/S8f1f29e17972433dbf8d46e85f600406c/Nepoagym-chemin-pour-femmes-tout-attach-coupe-ample-sport-Fitness-gymnastique.jpg_Q90.jpg_.webp",
        category: "Tank Tops",
        url: ["tank_tops"],
        see_more: ["tank_tops"]
      },
    ],
    [
      {
        img: "https://ae01.alicdn.com/kf/S812ca56a752d4907bd6abe7f1afb7ad8B/Mocassins-enfiler-en-maille-pour-femmes-chaussures-d-t-d-contract-es-la-mode-baskets-de.jpg_Q90.jpg_.webp",
        category: "",
        url: ["sneakers"],
        see_more: ["sneakers"]
      },
      {
        img: "https://ae01.alicdn.com/kf/H205dc1cc7067446581335736ad4447f1I/Bandeau-en-mati-re-antid-rapante-pour-le-tennis-grip-anti-sueur-aussi-pour-yoga-basket.jpg_Q90.jpg_.webps",
        category: "",
        url: ["accessories"],
        see_more: ["accessories"]
      },
      {
        img: "https://ae01.alicdn.com/kf/S353b7bf9733c43a49ab52a47ebf756a8x/Chaussures-semelles-compens-es-pour-femmes-baskets-en-maille-respirantes-et-d-contract-es-plates-et.jpg_640x640.jpg",
        category: "Sneakers",
        url: ["sneakers"],
        see_more: ["sneakers"]
      },
      {
        img: "https://ae01.alicdn.com/kf/HTB1SwPtXIrrK1Rjy1zeq6xalFXal/Chaussettes-de-Yoga-pour-femmes-en-coton-antid-rapantes-demi-orteils-pour-Ballet-Pilates-danse-Barre.jpg_Q90.jpg_.webp",
        category: "Accessories",
        url: ["accessories"],
        see_more: ["accessories"]
      },
    ],
  ]

  products_footer_left = [
    {
      type: 'leggings',
      url: 'https://fr.aliexpress.com/item/1005004588773214.html?spm=a2g0o.productlist.0.0.2c821e68QAsllI&algo_pvid=d3108726-fc88-4ee3-8b75-24f983232d8e&algo_exp_id=d3108726-fc88-4ee3-8b75-24f983232d8e-29&pdp_ext_f=%7B%22sku_id%22%3A%2212000029739857169%22%7D&pdp_npi=2%40dis%21MAD%21309.29%21185.6%21%21%21%21%21%402101e9d416600446359824444e554d%2112000029739857169%21sea&curPageLogUid=CLDF410f7Ql4',
      img_front: 'https://ae01.alicdn.com/kf/S5aa1a18dafa44a47a591a6cb7199a7934/Ensemble-de-2-pi-ces-de-Yoga-pour-femmes-soutien-gorge-Sexy-short-de-Sport-sans.jpg_Q90.jpg_.webp',
      img_back: 'https://ae01.alicdn.com/kf/S829d2653d4234dd5ae794c663cc986459/Ensemble-de-2-pi-ces-de-Yoga-pour-femmes-soutien-gorge-Sexy-short-de-Sport-sans.jpg_Q90.jpg_.webp',
      price: '$45.99',
      oldprice: '',
      description: 'Female 2 Pieces Fitness Outfit',
      star: 5,
      Reviews: 78,
      long_description: "----------------------------------------",
    },
    {

      type: 'leggings',
      url: 'https://fr.aliexpress.com/item/1005003081851639.html?spm=a2g0o.detail.100009.1.79d0437e9AljmA&gps-id=pcDetailLeftTopSell&scm=1007.13482.271138.0&scm_id=1007.13482.271138.0&scm-url=1007.13482.271138.0&pvid=8ec6f4fb-d511-4508-8e3a-7e17b5e523b9&_t=gps-id%3ApcDetailLeftTopSell%2Cscm-url%3A1007.13482.271138.0%2Cpvid%3A8ec6f4fb-d511-4508-8e3a-7e17b5e523b9%2Ctpp_buckets%3A668%232846%238109%231935&pdp_ext_f=%7B%22sku_id%22%3A%2212000023970125643%22%2C%22sceneId%22%3A%223482%22%7D&pdp_npi=2%40dis%21MAD%21322.7%21203.29%21%21%21%21%21%402101f6ba16600476390441323e1a6c%2112000023970125643%21rec&gatewayAdapt=glo2fra',
      img_front: "https://ae01.alicdn.com/kf/H62406e040eee4dceb2490e9976e5008ey/Ensemble-de-v-tements-de-sport-pour-femmes-soutien-gorge-et-Leggings-v-tements-d-entra.jpg_Q90.jpg_.webp",

      img_back: 'https://ae01.alicdn.com/kf/H43e7b0a443f24160994fd4fde92e0a73u/Ensemble-de-v-tements-de-sport-pour-femmes-soutien-gorge-et-Leggings-v-tements-d-entra.jpg_Q90.jpg_.webp',
      price: '$100.99',
      oldprice: '',
      description: '2 Pieces Set Sportwear Workout ',
      star: 5,
      Reviews: 65,
      long_description: "----------------------------------------",
    },
    {
      type: 'leggings',
      url: 'https://fr.aliexpress.com/item/1005003310164722.html?spm=a2g0o.detail.1000060.3.5d5e14c25fFJw1&gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.274681.0&scm_id=1007.13339.274681.0&scm-url=1007.13339.274681.0&pvid=9f15be36-8b29-403d-887f-5e40c83d4fff&_t=gps-id%3ApcDetailBottomMoreThisSeller%2Cscm-url%3A1007.13339.274681.0%2Cpvid%3A9f15be36-8b29-403d-887f-5e40c83d4fff%2Ctpp_buckets%3A668%232846%238109%231935&pdp_ext_f=%7B%22sku_id%22%3A%2212000026122999828%22%2C%22sceneId%22%3A%223339%22%7D&pdp_npi=2%40dis%21MAD%21240.07%21129.68%21%21%21%21%21%40210323a316600490541427441ea85b%2112000026122999828%21rec&gatewayAdapt=glo2fra',
      img_front: "https://ae01.alicdn.com/kf/S4cbf357fa5064efa901fcec12c69c4bad/Faux-d-bardeur-deux-pi-ces-pour-femmes-soutien-gorge-de-Sport-Fitness-Push-Up-sous.jpg_Q90.jpg_.webp",

      img_back: 'https://ae01.alicdn.com/kf/S846e14e0129e4ab6b9bab6ab0bd6fed6c/Faux-d-bardeur-deux-pi-ces-pour-femmes-soutien-gorge-de-Sport-Fitness-Push-Up-sous.jpg_Q90.jpg_.webp',
      price: '$29.00 ',
      oldprice: '',
      description: 'Sexy Push Up Sports Bras ',
      star: 5,
      Reviews: 56,
      long_description: "----------------------------------------",
    },
    {
      type: 'leggings',
      url: 'https://fr.aliexpress.com/item/1005004271724086.html?spm=a2g0o.productlist.0.0.5e3253bazEPv3h&algo_pvid=23d1a82f-8f01-48e0-9e1e-b6df1db903c8&algo_exp_id=23d1a82f-8f01-48e0-9e1e-b6df1db903c8-29&pdp_ext_f=%7B%22sku_id%22%3A%2212000028585631196%22%7D&pdp_npi=2%40dis%21MAD%2146.32%210.1%21%21%21%21%21%4021031a5516600506651047574e426e%2112000028585631196%21sea&curPageLogUid=zaadAJzbVDZc&gatewayAdapt=glo2fra',
      img_front: "https://ae01.alicdn.com/kf/S58522944ceb34a789d89071dbf6ee5b20/Tapis-de-Massage-lectrique-pour-les-pieds-stimulateur-musculaire-am-liore-la-Circulation-sanguine-soulage-les.jpg_Q90.jpg_.webp",

      img_back: 'https://ae01.alicdn.com/kf/Se3352ed59b6043989be7f4910e7b94beO/Tapis-de-Massage-lectrique-pour-les-pieds-stimulateur-musculaire-am-liore-la-Circulation-sanguine-soulage-les.jpg_Q90.jpg_.webp',
      price: '$19.00 ',
      oldprice: '',
      description: 'Electric Foot Massage Improve The Circulation',
      star: 5,
      Reviews: 60,
      long_description: "----------------------------------------",
    },

  ]
  products_footer_right = [
    {
      type: 'leggings',
      url: 'https://fr.aliexpress.com/item/1005004271724086.html?spm=a2g0o.productlist.0.0.5e3253bazEPv3h&algo_pvid=23d1a82f-8f01-48e0-9e1e-b6df1db903c8&algo_exp_id=23d1a82f-8f01-48e0-9e1e-b6df1db903c8-29&pdp_ext_f=%7B%22sku_id%22%3A%2212000028585631196%22%7D&pdp_npi=2%40dis%21MAD%2146.32%210.1%21%21%21%21%21%4021031a5516600506651047574e426e%2112000028585631196%21sea&curPageLogUid=zaadAJzbVDZc&gatewayAdapt=glo2fra',
      img_front: "https://ae01.alicdn.com/kf/H55a871f373574d8c96824c264ed0bf8dR.jpg",

      img_back: 'https://ae01.alicdn.com/kf/H81e83838bbfe4f8594d674ff1155f286f.jpg',
      price: '$30.99 ',
      oldprice: '',
      description: 'Sleeveless Tank Tops Summer Casual Black',
      star: 5,
      Reviews: 79,
      long_description: "----------------------------------------",
    },
    {
      type: 'leggings',
      url: 'https://fr.aliexpress.com/item/4000668525721.html?spm=a2g0o.productlist.0.0.5fdf77a2cZ3E6X&algo_pvid=186f0a73-31be-4d74-ba39-da5e7397a126&algo_exp_id=186f0a73-31be-4d74-ba39-da5e7397a126-25&pdp_ext_f=%7B%22sku_id%22%3A%2212000028609110430%22%7D&pdp_npi=2%40dis%21MAD%2128.58%2120.01%21%21%21%21%21%40210318cb16600502790255577e3e56%2112000028609110430%21sea&curPageLogUid=bunZixMjTeNd&gatewayAdapt=glo2fra',
      img_front: "https://ae01.alicdn.com/kf/He00a46aff0bb42f990b7dabda5765e649/Chaussettes-de-Yoga-antid-rapantes-de-haute-qualit-pour-femmes-bandes-en-coton-amortissantes-s-chage.jpg_Q90.jpg_.webp",

      img_back: 'https://ae01.alicdn.com/kf/H898c45dfaaf046a9aedd27d45c46dfb9X/Chaussettes-de-Yoga-antid-rapantes-de-haute-qualit-pour-femmes-bandes-en-coton-amortissantes-s-chage.jpg_Q90.jpg_.webp',
      price: '$16.00 ',
      oldprice: '',
      description: 'Barre Socks',
      star: 5,
      Reviews: 46,
      long_description: "----------------------------------------",
    },
    {
      type: 'leggings',
      url: 'https://fr.aliexpress.com/item/4001049023205.html?spm=a2g0o.detail.1000014.11.58d5351bmVimw0&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40000.267768.0&scm_id=1007.40000.267768.0&scm-url=1007.40000.267768.0&pvid=d5b5d235-8320-4c94-9786-c7a8e8455a6d&_t=gps-id:pcDetailBottomMoreOtherSeller,scm-url:1007.40000.267768.0,pvid:d5b5d235-8320-4c94-9786-c7a8e8455a6d,tpp_buckets:668%232846%238109%23257&pdp_ext_f=%7B%22sku_id%22%3A%2212000021684872460%22%2C%22sceneId%22%3A%2230050%22%7D&pdp_npi=2%40dis%21MAD%21323.15%21145.41%21%21%21%21%21%402101d1bd16612497728496038e1a10%2112000021684872460%21rec',
      img_front: "https://ae01.alicdn.com/kf/H8639991637c6471cbe396dc1d4fa16f4R/Baskets-en-maille-pour-hommes-chaussures-d-t-respirantes-de-haute-qualit-d-contract-es.jpg_Q90.jpg_.webp",

      img_back: 'https://ae01.alicdn.com/kf/H369a027fe90442bca2e5151c3d796e10z/Baskets-en-maille-pour-hommes-chaussures-d-t-respirantes-de-haute-qualit-d-contract-es.jpg_Q90.jpg_.webp',
      price: '$35.50 ',
      oldprice: '',
      description: 'Sneakers Comfort Casual for Women Workout',
      star: 5,
      Reviews: 51,
      long_description: "----------------------------------------",
    },
    {
      type: 'leggings',
      url: 'https://fr.aliexpress.com/item/4000835076990.html?spm=a2g0o.productlist.0.0.f5f15614U2nCN2&algo_pvid=da1e78e7-35cb-4063-814a-a4008bd572b8&algo_exp_id=da1e78e7-35cb-4063-814a-a4008bd572b8-13&pdp_ext_f=%7B%22sku_id%22%3A%2210000008705584946%22%7D&pdp_npi=2%40dis%21MAD%2147.81%2130.13%21%21%212.3%21%21%402103255b16612500301022452e6c38%2110000008705584946%21sea&curPageLogUid=VtGVKOXO6TBM',
      img_front: "https://ae01.alicdn.com/kf/H205dc1cc7067446581335736ad4447f1I/Bandeau-en-mati-re-antid-rapante-pour-le-tennis-grip-anti-sueur-aussi-pour-yoga-basket.jpg_Q90.jpg_.webp",

      img_back: 'https://ae01.alicdn.com/kf/H3d55d0155a06454d95afdc38424f9e786/Bandeau-en-mati-re-antid-rapante-pour-le-tennis-grip-anti-sueur-aussi-pour-yoga-basket.jpg_Q90.jpg_.webp',
      price: '$99.00 ',
      oldprice: '',
      description: 'Headband Sports Hear',
      star: 5,
      Reviews: 58,
      long_description: "----------------------------------------",
    },
  ]
 

}