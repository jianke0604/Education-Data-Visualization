<template>
    <div class="bgpage">
        <Header></Header>
        <!-- 用两个box作为示例，具体使用请自行更改 -->
        <div>
            <div class="container">
                <div class="box">
                    <Viewbox
                        :title="subTitle"
                        :boxb="true"
                    />
                </div>
                <div class="box">
                    <Viewbox
                        :title="subTitle"
                        :boxb="true"
                    />
                </div>
                <div class="box">
                    <Viewbox
                        :title="subTitle"
                        :boxb="true"
                    >
                    </Viewbox>
                </div>
            </div>
            <div class="container">
                <div class="box">
                    <Viewbox
                        title="测试子标题"
                        :boxb="true"
                    />
                </div>
                <div class="box">
                    <Viewbox
                        title="测试子标题"
                        :boxb="true"
                    />
                </div>
            </div>
            
        </div>
    </div>
    <div id="secondpart" style="width: 100%; height: 600px;"></div>
</template>

// TODO:  找到一个能恰当表示点大小的函数 + 把数据的划分粒度降低到半天

<script>
import Header from './Header.vue'
import Viewbox from './viewbox/Viewbox.vue'
import * as echarts from 'echarts'
export default {
    components: {
        Header,
        Viewbox
    },
    data() {
        return {
            subTitle: "子标题",
            data: [[2023, 8, 31, 0.2430939226519337, 44, 181, 'r8S3g', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 9, 1, 0.20553359683794467, 52, 253, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 2, 0.2328767123287671, 34, 146, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS'], [2023, 9, 3, 0.4536082474226804, 44, 97, 'm3D1v', 'Question_ZTbD7mxr2OUp8Fz6iNjy'], [2023, 9, 4, 0.24915254237288137, 147, 590, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 5, 0.2401500938086304, 128, 533, 'y9W5d', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 6, 0.1762414800389484, 181, 1027, 't5V9e', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 7, 0.28346456692913385, 216, 762, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS'], [2023, 9, 8, 0.26294277929155313, 193, 734, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 9, 0.20207852193995382, 350, 1732, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 10, 0.29014598540145986, 318, 1096, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 9, 11, 0.22893006575014943, 383, 1673, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 12, 0.2618556701030928, 381, 1455, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 13, 0.19611414693381907, 646, 3294, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 14, 0.21647940074906366, 289, 1335, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 15, 0.179813401187447, 212, 1179, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 16, 0.17955911823647294, 448, 2495, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 17, 0.2251655629139073, 442, 1963, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 18, 0.22137404580152673, 551, 2489, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS'], [2023, 9, 19, 0.24693877551020407, 242, 980, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS'], [2023, 9, 20, 0.19685767097966728, 213, 1082, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 9, 21, 0.15946502057613168, 155, 972, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW'], [2023, 9, 22, 0.20913107511045656, 426, 2037, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 23, 0.22405271828665568, 136, 607, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo'], [2023, 9, 24, 0.19586374695863748, 161, 822, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd'], [2023, 9, 25, 0.2016260162601626, 248, 1230, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW'], [2023, 9, 26, 0.16680429397192403, 202, 1211, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 9, 27, 0.2760041194644696, 268, 971, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW'], [2023, 9, 28, 0.24742268041237114, 384, 1552, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 29, 0.21915215745647237, 579, 2642, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 9, 30, 0.21471861471861473, 248, 1155, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 10, 1, 0.19837758112094395, 269, 1356, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 2, 0.23520853540252182, 485, 2062, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 10, 3, 0.18615314076111875, 406, 2181, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS'], [2023, 10, 4, 0.2063705697622252, 460, 2229, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 10, 5, 0.1926751592356688, 605, 3140, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS'], [2023, 10, 6, 0.20415126528291158, 718, 3517, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H'], [2023, 10, 7, 0.23214285714285715, 754, 3248, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW'], [2023, 10, 8, 0.22073474470734744, 709, 3212, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 9, 0.25081610446137104, 922, 3676, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 10, 0.23041189222669556, 744, 3229, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 11, 0.21982032565974172, 783, 3562, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 12, 0.23079128440366972, 805, 3488, 'm3D1v', 'Question_h7pXNg80nJbw1C4kAPRm'], [2023, 10, 13, 0.23212360761767875, 646, 2783, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd'], [2023, 10, 14, 0.2688570106432207, 581, 2161, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 15, 0.2209119496855346, 562, 2544, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 16, 0.2339734920205572, 865, 3697, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 17, 0.24084896954783144, 783, 3251, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW'], [2023, 10, 18, 0.21315529179030662, 862, 4044, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW'], [2023, 10, 19, 0.24736533957845433, 845, 3416, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 20, 0.23360790774299836, 709, 3035, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31'], [2023, 10, 21, 0.21636085626911314, 566, 2616, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 22, 0.23707117255504354, 463, 1953, 'm3D1v', 'Question_7NJzCXUPcvQF4Mkfh9Wr'], [2023, 10, 23, 0.24676233811690584, 705, 2857, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd'], [2023, 10, 24, 0.23995127892813642, 591, 2463, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31'], [2023, 10, 25, 0.25097360450021633, 580, 2311, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW'], [2023, 10, 26, 0.2161186848436247, 539, 2494, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd'], [2023, 10, 27, 0.2075623491552695, 258, 1243, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 10, 28, 0.22102231821454282, 307, 1389, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf'], [2023, 10, 29, 0.2764378478664193, 447, 1617, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo'], [2023, 10, 30, 0.2811550151975684, 555, 1974, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd'], [2023, 10, 31, 0.26320501342882724, 588, 2234, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 1, 0.20477568740955138, 566, 2764, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 2, 0.223963133640553, 486, 2170, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3'], [2023, 11, 3, 0.209994952044422, 416, 1981, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc'], [2023, 11, 4, 0.17664670658682635, 472, 2672, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo'], [2023, 11, 5, 0.21694214876033058, 420, 1936, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 6, 0.25440806045340053, 505, 1985, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31'], [2023, 11, 7, 0.2668024439918534, 524, 1964, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31'], [2023, 11, 8, 0.2168296089385475, 621, 2864, 'm3D1v', 'Question_Jr4Wz5jLqmN01KUwHa7g'], [2023, 11, 9, 0.22131565527791944, 434, 1961, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu'], [2023, 11, 10, 0.1810512654120701, 279, 1541, 'm3D1v', 'Question_Ou3f2Wt9BqExm5DpN7Zk'], [2023, 11, 11, 0.16303583977512298, 232, 1423, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf'], [2023, 11, 12, 0.20657276995305165, 396, 1917, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31'], [2023, 11, 13, 0.2079866888519135, 500, 2404, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc'], [2023, 11, 14, 0.2663316582914573, 530, 1990, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31'], [2023, 11, 15, 0.23326359832635984, 669, 2868, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL'], [2023, 11, 16, 0.24373795761078998, 506, 2076, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc'], [2023, 11, 17, 0.24685138539042822, 392, 1588, 'm3D1v', 'Question_Mh4CZIsrEfxkP1wXtOYV'], [2023, 11, 18, 0.19300605245460659, 287, 1487, 'm3D1v', 'Question_62XbhBvJ8NUSnApgDL94'], [2023, 11, 19, 0.24599615631005767, 384, 1561, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc'], [2023, 11, 20, 0.23459347488348006, 453, 1931, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31'], [2023, 11, 21, 0.24050632911392406, 608, 2528, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 22, 0.2680029695619896, 722, 2694, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31'], [2023, 11, 23, 0.22701149425287356, 711, 3132, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 24, 0.26867119301648884, 554, 2062, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 25, 0.26487625065824116, 503, 1899, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 26, 0.2907622412922766, 576, 1981, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ'], [2023, 11, 27, 0.25949367088607594, 656, 2528, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL'], [2023, 11, 28, 0.2720812182741117, 536, 1970, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 29, 0.30440967283072545, 642, 2109, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 11, 30, 0.25234697709350357, 672, 2663, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 1, 0.29122155132373434, 627, 2153, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 2, 0.28917609046849757, 537, 1857, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 3, 0.29112008072653883, 577, 1982, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 4, 0.26666666666666666, 484, 1815, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 5, 0.3467137185707984, 786, 2267, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 6, 0.27790973871733965, 819, 2947, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 7, 0.2631578947368421, 430, 1634, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 8, 0.2895460797799175, 421, 1454, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 9, 0.33236574746008707, 458, 1378, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc'], [2023, 12, 10, 0.24789410348977137, 206, 831, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2023, 12, 11, 0.2315112540192926, 216, 933, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ'], [2023, 12, 12, 0.3354350567465322, 532, 1586, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL'], [2023, 12, 13, 0.3081172970675733, 725, 2353, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2023, 12, 14, 0.3001215066828676, 494, 1646, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2023, 12, 15, 0.27426955702167766, 291, 1061, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 16, 0.26145038167938933, 548, 2096, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2023, 12, 17, 0.3968503937007874, 252, 635, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ'], [2023, 12, 18, 0.3171355498721228, 248, 782, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3'], [2023, 12, 19, 0.35873472322070454, 499, 1391, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3'], [2023, 12, 20, 0.36932192231731403, 561, 1519, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3'], [2023, 12, 21, 0.35622710622710624, 389, 1092, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 22, 0.274831243972999, 285, 1037, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3'], [2023, 12, 23, 0.2962962962962963, 368, 1242, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 24, 0.3437945791726106, 241, 701, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc'], [2023, 12, 25, 0.3441108545034642, 298, 866, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O'], [2023, 12, 26, 0.397796817625459, 325, 817, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2023, 12, 27, 0.390745501285347, 304, 778, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ'], [2023, 12, 28, 0.39770114942528734, 346, 870, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf'], [2023, 12, 29, 0.4298245614035088, 294, 684, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2023, 12, 30, 0.4131455399061033, 616, 1491, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2023, 12, 31, 0.5170532060027285, 379, 733, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2024, 1, 1, 0.43037974683544306, 306, 711, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3'], [2024, 1, 2, 0.41254523522316044, 342, 829, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe'], [2024, 1, 3, 0.4033898305084746, 238, 590, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ'], [2024, 1, 4, 0.4887640449438202, 87, 178, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W'], [2024, 1, 5, 0.4336569579288026, 134, 309, 'm3D1v', 'Question_Mh4CZIsrEfxkP1wXtOYV'], [2024, 1, 6, 0.57421875, 147, 256, 'm3D1v', 'Question_hZ5wXofebmTlzKB1jNcP'], [2024, 1, 7, 0.5688073394495413, 62, 109, 'g7R2j', 'Question_hZ5wXofebmTlzKB1jNcP'], [2024, 1, 8, 0.732620320855615, 137, 187, 'm3D1v', 'Question_bumGRTJ0c8p4v5D6eHZa'], [2024, 1, 9, 0.5463917525773195, 53, 97, 'y9W5d', 'Question_FNg8X9v5zcbB1tQrxHR3'], [2024, 1, 10, 0.4735812133072407, 242, 511, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ'], [2024, 1, 11, 0.9047619047619048, 19, 21, 'g7R2j', 'Question_bumGRTJ0c8p4v5D6eHZa'], [2024, 1, 12, 0.38461538461538464, 5, 13, 'y9W5d', 'Question_Mh4CZIsrEfxkP1wXtOYV'], [2024, 1, 13, 0.8846153846153846, 23, 26, 'y9W5d', 'Question_Mh4CZIsrEfxkP1wXtOYV'], [2024, 1, 14, 0.4479495268138801, 142, 317, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe'], [2024, 1, 15, 0.6521739130434783, 30, 46, 'y9W5d', 'Question_xqlJkmRaP0otZcX4fK3W'], [2024, 1, 16, 0.5666666666666667, 17, 30, 'b3C9s', 'Question_xqlJkmRaP0otZcX4fK3W'], [2024, 1, 20, 0.3333333333333333, 2, 6, 'g7R2j', 'Question_X3wF8QlTyi4mZkDp9Kae'], [2024, 1, 21, 0.8888888888888888, 8, 9, 'm3D1v', 'Question_h7pXNg80nJbw1C4kAPRm'], [2024, 1, 22, 0.2, 1, 5, 'r8S3g', 'Question_VgKw8PjY1FR6cm2QI9XW'], [2024, 1, 23, 1.0, 1, 1, 't5V9e', 'Question_3oPyUzDmQtcMfLpGZ0jW'], [2024, 1, 25, 1.0, 3, 3, 'g7R2j', 'Question_5fgqjSBwTPG7KUV3it6O']]
        }
    }, 
    mounted() {
        this.draw_part_2();
    },
    methods: {
        draw_part_2() {
            const draw = () => {
            this.data_parse();
            var chartDom = document.getElementById('secondpart');
            // var chartDom = this.$refs.secondpart;
            console.log(chartDom)
            var myChart = echarts.init(chartDom);
            var option;
            var data1 = [];
            var data2 = [];
            var data3 = [];
            var random = function (max) {
            return (Math.random() * max).toFixed(3);
            };
            for (var i = 0; i < 500; i++) {
            data1.push([random(15), random(10), random(1)]);
            data2.push([random(10), random(10), random(1)]);
            data3.push([random(15), random(10), random(1)]);
            }
            option = {
            animation: false,
            legend: {
                data: ['每日数据']
            },
            tooltip: {
                show: true,
                formatter: function (param) {
                    const info = param.data;
                    return `日期: ${info[0]}<br>
                            今日通过率: ${info[1]}<br>
                            今日总通过次数: ${info[2]}<br>
                            今日总提交次数: ${info[3]}<br>
                            今日热门知识点: ${info[4]}<br>
                            今日热门题目: ${info[5]}<br>        
                            `;
                }
            },
            xAxis: {
                type: 'time',
                // min: 'dataMin',
                // max: 'dataMax',
                splitLine: {
                show: true
                },
                axisLabel: {
                    formatter: function (value) {
                        // Format the date
                        return echarts.format.formatTime('yyyy-MM-dd', value);
                    }
                }
            },
            yAxis: {
                type: 'value',
                min: 'dataMin',
                max: 'dataMax',
                splitLine: {
                show: true
                }
            },
            dataZoom: [
                {
                type: 'slider',
                show: true,
                xAxisIndex: [0],
                start: 1,
                end: 35
                },
                {
                type: 'slider',
                show: true,
                yAxisIndex: [0],
                left: '93%',
                start: 29,
                end: 36
                },
                {
                type: 'inside',
                xAxisIndex: [0],
                start: 1,
                end: 35
                },
                {
                type: 'inside',
                yAxisIndex: [0],
                start: 29,
                end: 36
                }
            ],
            series: [
                {
                name: '每日数据',
                type: 'scatter',
                itemStyle: {
                    normal: {
                    opacity: 0.8
                    }
                },
                symbolSize: function (val) {
                    return val[3] / 50;
                },
                data: this.data
                }
            ]
            };

            option && myChart.setOption(option);
            };
            if (document.readyState === 'complete') {   
                draw();
            } else {
                window.onload = draw;
            }
        },
        data_parse() {
            for (let i = 0; i < this.data.length; i++) {
                const year = this.data[i][0];
                const month = this.data[i][1];
                const day = this.data[i][2];
                this.data[i].splice(0, 3, `${year}-${month}-${day}`);
                // this.data[i][0] = new Date(this.data[i][0]);
            }
            console.log(this.data);
        }
    }

}
</script>


<style>
.bgpage{
    background: url(src/assets/true.png);
    height: 90vh;
    width: 100vw;
}
.container {
    display: flex; /* 将容器设置为 flex 容器 */
}
.box {
    flex: 1; /* 每个子元素占据相等的空间 */
    height: 300px;
    margin: 10px;
}
</style>