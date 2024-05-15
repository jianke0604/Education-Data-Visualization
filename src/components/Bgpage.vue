<template>
    <!-- <div class="bgpage">
        <Header></Header>
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
    </div> -->
    <div id="secondpart" style="width: 100%; height: 600px;"></div>
    <div id="app">
    <Scatter3DChart style="width: 100%; height: 500px;"></Scatter3DChart>
  </div>
</template>

<script>
import Scatter3DChart from './Scatter3DChart.vue';
import Header from './Header.vue'
import Viewbox from './viewbox/Viewbox.vue'
import * as echarts from 'echarts'
export default {
    components: {
        Header,
        Viewbox,
        Scatter3DChart
    },
    data() {
        return {
            subTitle: "子标题",
            data: [[2023, 8, 31, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 8, 31, 0.4166666666666667, 10, 24, 'r8S3g', 'Question_VgKw8PjY1FR6cm2QI9XW', 'day'], [2023, 8, 31, 0.21656050955414013, 34, 157, 'r8S3g', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 9, 1, 0.17647058823529413, 3, 17, 'm3D1v', 'Question_tgOjrpZLw4RdVzQx85h6', 'midnight'], [2023, 9, 1, 0.20930232558139536, 36, 172, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 9, 1, 0.203125, 13, 64, 'r8S3g', 'Question_VgKw8PjY1FR6cm2QI9XW', 'night'], [2023, 9, 2, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 9, 2, 0.24444444444444444, 11, 45, 't5V9e', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 9, 2, 0.22772277227722773, 23, 101, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'night'], [2023, 9, 3, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 9, 3, 0.4444444444444444, 20, 45, 'm3D1v', 'Question_BW0ItEaymH3TkD6S15JF', 'day'], [2023, 9, 3, 0.46153846153846156, 24, 52, 'm3D1v', 'Question_ZTbD7mxr2OUp8Fz6iNjy', 'night'], [2023, 9, 4, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 9, 4, 0.27058823529411763, 46, 170, 'r8S3g', 'Question_VgKw8PjY1FR6cm2QI9XW', 'day'], [2023, 9, 4, 0.24047619047619048, 101, 420, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 5, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 9, 5, 0.36, 63, 175, 'r8S3g', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 9, 5, 0.18156424581005587, 65, 358, 'y9W5d', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 6, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 9, 6, 0.15736040609137056, 124, 788, 'r8S3g', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 9, 6, 0.2384937238493724, 57, 239, 't5V9e', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 7, 0.3700787401574803, 47, 127, 'm3D1v', 'Question_7NJzCXUPcvQF4Mkfh9Wr', 'midnight'], [2023, 9, 7, 0.2631578947368421, 80, 304, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'day'], [2023, 9, 7, 0.2688821752265861, 89, 331, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 8, 0.5, 1, 2, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'midnight'], [2023, 9, 8, 0.26443768996960487, 87, 329, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 9, 8, 0.26054590570719605, 105, 403, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 9, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 9, 9, 0.1920704845814978, 218, 1135, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'day'], [2023, 9, 9, 0.22110552763819097, 132, 597, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 10, 0.6666666666666666, 2, 3, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'midnight'], [2023, 9, 10, 0.24213075060532688, 100, 413, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 9, 10, 0.3176470588235294, 216, 680, 'm3D1v', 'Question_BW0ItEaymH3TkD6S15JF', 'night'], [2023, 9, 11, 0.192, 24, 125, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'midnight'], [2023, 9, 11, 0.24116161616161616, 191, 792, 'm3D1v', 'Question_VgKw8PjY1FR6cm2QI9XW', 'day'], [2023, 9, 11, 0.2222222222222222, 168, 756, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 12, 0.5384615384615384, 7, 13, 't5V9e', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'midnight'], [2023, 9, 12, 0.224283305227656, 133, 593, 'm3D1v', 'Question_h7pXNg80nJbw1C4kAPRm', 'day'], [2023, 9, 12, 0.2838633686690224, 241, 849, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'night'], [2023, 9, 13, 0.13333333333333333, 2, 15, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'midnight'], [2023, 9, 13, 0.2306525037936267, 304, 1318, 'm3D1v', 'Question_VgKw8PjY1FR6cm2QI9XW', 'day'], [2023, 9, 13, 0.17338092809790923, 340, 1961, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 14, 0.0, 0, 1, 'm3D1v', 'Question_Jr4Wz5jLqmN01KUwHa7g', 'midnight'], [2023, 9, 14, 0.25164113785557984, 115, 457, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'day'], [2023, 9, 14, 0.19840364880273662, 174, 877, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 15, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 9, 15, 0.16973415132924335, 83, 489, 'm3D1v', 'Question_BW0ItEaymH3TkD6S15JF', 'day'], [2023, 9, 15, 0.18695652173913044, 129, 690, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 16, 1.0, 2, 2, 'r8S3g', 'Question_rvB9mVE6Kbd8jAY4NwPx', 'midnight'], [2023, 9, 16, 0.2087378640776699, 172, 824, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 9, 16, 0.16417016177351706, 274, 1669, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'night'], [2023, 9, 17, 0.2962962962962963, 8, 27, 'r8S3g', 'Question_q7OpB2zCMmW9wS8uNt3H', 'midnight'], [2023, 9, 17, 0.2260536398467433, 177, 783, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 9, 17, 0.22289679098005205, 257, 1153, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 18, 1.0, 1, 1, 'r8S3g', 'Question_VgKw8PjY1FR6cm2QI9XW', 'midnight'], [2023, 9, 18, 0.23842364532019705, 242, 1015, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'day'], [2023, 9, 18, 0.2090970807875085, 308, 1473, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'night'], [2023, 9, 19, 0.0, 0, 2, 'r8S3g', 'Question_fZrP3FJ4ebUogW9V7taS', 'midnight'], [2023, 9, 19, 0.26520681265206814, 109, 411, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'day'], [2023, 9, 19, 0.2345679012345679, 133, 567, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'night'], [2023, 9, 20, 0.2, 1, 5, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'midnight'], [2023, 9, 20, 0.20098039215686275, 82, 408, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'day'], [2023, 9, 20, 0.19431988041853512, 130, 669, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 9, 21, 0.35714285714285715, 5, 14, 't5V9e', 'Question_QRm48lXxzdP7Tn1WgNOf', 'midnight'], [2023, 9, 21, 0.1735159817351598, 38, 219, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'day'], [2023, 9, 21, 0.15155615696887687, 112, 739, 'm3D1v', 'Question_tgOjrpZLw4RdVzQx85h6', 'night'], [2023, 9, 22, 0.08333333333333333, 2, 24, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'midnight'], [2023, 9, 22, 0.24583333333333332, 177, 720, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 9, 22, 0.19102861562258314, 247, 1293, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'night'], [2023, 9, 23, 0.5714285714285714, 12, 21, 'm3D1v', 'Question_h7pXNg80nJbw1C4kAPRm', 'midnight'], [2023, 9, 23, 0.2360248447204969, 38, 161, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'day'], [2023, 9, 23, 0.2023529411764706, 86, 425, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'night'], [2023, 9, 24, 0.2857142857142857, 2, 7, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'midnight'], [2023, 9, 24, 0.18181818181818182, 76, 418, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'day'], [2023, 9, 24, 0.20906801007556675, 83, 397, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'night'], [2023, 9, 25, 0.0, 0, 12, 'm3D1v', 'Question_NixCn84GdK2tySa5rB1V', 'midnight'], [2023, 9, 25, 0.1932367149758454, 120, 621, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 9, 25, 0.21440536013400335, 128, 597, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'night'], [2023, 9, 26, 1.0, 1, 1, 'r8S3g', 'Question_q7OpB2zCMmW9wS8uNt3H', 'midnight'], [2023, 9, 26, 0.15769944341372913, 85, 539, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'day'], [2023, 9, 26, 0.17287630402384502, 116, 671, 'm3D1v', 'Question_BW0ItEaymH3TkD6S15JF', 'night'], [2023, 9, 27, 0.5, 1, 2, 'm3D1v', 'Question_Jr4Wz5jLqmN01KUwHa7g', 'midnight'], [2023, 9, 27, 0.25, 100, 400, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 9, 27, 0.29349736379613356, 167, 569, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'night'], [2023, 9, 28, 0.3333333333333333, 2, 6, 't5V9e', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'midnight'], [2023, 9, 28, 0.31501340482573725, 235, 746, 'm3D1v', 'Question_VgKw8PjY1FR6cm2QI9XW', 'day'], [2023, 9, 28, 0.18375, 147, 800, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 29, 0.2, 6, 30, 't5V9e', 'Question_3MwAFlmNO8EKrpY5zjUd', 'midnight'], [2023, 9, 29, 0.2446215139442231, 307, 1255, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 9, 29, 0.19602063375092116, 266, 1357, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 9, 30, 0.2857142857142857, 14, 49, 't5V9e', 'Question_3MwAFlmNO8EKrpY5zjUd', 'midnight'], [2023, 9, 30, 0.23053892215568864, 154, 668, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 9, 30, 0.182648401826484, 80, 438, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'night'], [2023, 10, 1, 0.18181818181818182, 4, 22, 'b3C9s', 'Question_FNg8X9v5zcbB1tQrxHR3', 'midnight'], [2023, 10, 1, 0.188911704312115, 184, 974, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 10, 1, 0.225, 81, 360, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'night'], [2023, 10, 2, 0.15178571428571427, 17, 112, 'r8S3g', 'Question_fZrP3FJ4ebUogW9V7taS', 'midnight'], [2023, 10, 2, 0.2375586854460094, 253, 1065, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 10, 2, 0.24293785310734464, 215, 885, 'm3D1v', 'Question_x2L7AqbMuTjCwPFy6vNr', 'night'], [2023, 10, 3, 0.0, 0, 8, 's8Y2f', 'Question_x2Fy7rZ3SwYl9jMQkpOD', 'midnight'], [2023, 10, 3, 0.2012779552715655, 189, 939, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'day'], [2023, 10, 3, 0.17585089141004862, 217, 1234, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 4, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 10, 4, 0.2272, 142, 625, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'day'], [2023, 10, 4, 0.19825436408977556, 318, 1604, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 10, 5, 0.13333333333333333, 12, 90, 'r8S3g', 'Question_q7OpB2zCMmW9wS8uNt3H', 'midnight'], [2023, 10, 5, 0.17455621301775148, 177, 1014, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 10, 5, 0.2043222003929273, 416, 2036, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'night'], [2023, 10, 6, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 10, 6, 0.2175226586102719, 216, 993, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 10, 6, 0.1988906497622821, 502, 2524, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 7, 0.08333333333333333, 1, 12, 'm3D1v', 'Question_7NJzCXUPcvQF4Mkfh9Wr', 'midnight'], [2023, 10, 7, 0.266803840877915, 389, 1458, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'day'], [2023, 10, 7, 0.2047244094488189, 364, 1778, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 10, 8, 0.20987654320987653, 17, 81, 'r8S3g', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'midnight'], [2023, 10, 8, 0.20302547770700638, 255, 1256, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'day'], [2023, 10, 8, 0.23306666666666667, 437, 1875, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 9, 0.4927536231884058, 34, 69, 'r8S3g', 'Question_q7OpB2zCMmW9wS8uNt3H', 'midnight'], [2023, 10, 9, 0.22369291859695567, 338, 1511, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 10, 9, 0.26240458015267176, 550, 2096, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'night'], [2023, 10, 10, 0.30303030303030304, 20, 66, 'r8S3g', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'midnight'], [2023, 10, 10, 0.26881720430107525, 250, 930, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 10, 10, 0.2122704881325571, 474, 2233, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 11, 0.14814814814814814, 8, 54, 't5V9e', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'midnight'], [2023, 10, 11, 0.22536806342015855, 199, 883, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 10, 11, 0.21942857142857142, 576, 2625, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 12, 0.2857142857142857, 8, 28, 'm3D1v', 'Question_x2L7AqbMuTjCwPFy6vNr', 'midnight'], [2023, 10, 12, 0.2713841368584759, 349, 1286, 'm3D1v', 'Question_h7pXNg80nJbw1C4kAPRm', 'day'], [2023, 10, 12, 0.20607175712971482, 448, 2174, 'm3D1v', 'Question_h7pXNg80nJbw1C4kAPRm', 'night'], [2023, 10, 13, 0.15789473684210525, 9, 57, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'midnight'], [2023, 10, 13, 0.20374531835205992, 272, 1335, 'm3D1v', 'Question_q7OpB2zCMmW9wS8uNt3H', 'day'], [2023, 10, 13, 0.26240115025161753, 365, 1391, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'night'], [2023, 10, 14, 0.19047619047619047, 8, 42, 'y9W5d', 'Question_QRm48lXxzdP7Tn1WgNOf', 'midnight'], [2023, 10, 14, 0.23756345177664975, 234, 985, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'day'], [2023, 10, 14, 0.29894179894179895, 339, 1134, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'night'], [2023, 10, 15, 0.3669064748201439, 51, 139, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'midnight'], [2023, 10, 15, 0.2125912408759124, 233, 1096, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'day'], [2023, 10, 15, 0.21237585943468296, 278, 1309, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 16, 0.0, 0, 78, 't5V9e', 'Question_x2L7AqbMuTjCwPFy6vNr', 'midnight'], [2023, 10, 16, 0.21760524876981957, 398, 1829, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'day'], [2023, 10, 16, 0.2608938547486033, 467, 1790, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'night'], [2023, 10, 17, 0.20408163265306123, 20, 98, 'r8S3g', 'Question_3MwAFlmNO8EKrpY5zjUd', 'midnight'], [2023, 10, 17, 0.23742138364779874, 302, 1272, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'day'], [2023, 10, 17, 0.24508240297713982, 461, 1881, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'night'], [2023, 10, 18, 0.14788732394366197, 21, 142, 't5V9e', 'Question_fZrP3FJ4ebUogW9V7taS', 'midnight'], [2023, 10, 18, 0.2358356940509915, 333, 1412, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'day'], [2023, 10, 18, 0.20401606425702812, 508, 2490, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'night'], [2023, 10, 19, 0.15384615384615385, 20, 130, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'midnight'], [2023, 10, 19, 0.23232908458864426, 401, 1726, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 10, 19, 0.2717948717948718, 424, 1560, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'night'], [2023, 10, 20, 0.4782608695652174, 22, 46, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'midnight'], [2023, 10, 20, 0.221671388101983, 313, 1412, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'day'], [2023, 10, 20, 0.23715916296766013, 374, 1577, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'night'], [2023, 10, 21, 0.23469387755102042, 23, 98, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'midnight'], [2023, 10, 21, 0.19939804364183597, 265, 1329, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'day'], [2023, 10, 21, 0.23380992430613962, 278, 1189, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 22, 0.29411764705882354, 15, 51, 't5V9e', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'midnight'], [2023, 10, 22, 0.2548076923076923, 265, 1040, 'm3D1v', 'Question_7NJzCXUPcvQF4Mkfh9Wr', 'day'], [2023, 10, 22, 0.2122969837587007, 183, 862, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 23, 0.0603448275862069, 7, 116, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'midnight'], [2023, 10, 23, 0.28242320819112626, 331, 1172, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'day'], [2023, 10, 23, 0.23390694710006374, 367, 1569, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'night'], [2023, 10, 24, 0.15172413793103448, 22, 145, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'midnight'], [2023, 10, 24, 0.23275862068965517, 216, 928, 'm3D1v', 'Question_BW0ItEaymH3TkD6S15JF', 'day'], [2023, 10, 24, 0.2539568345323741, 353, 1390, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 25, 0.4, 2, 5, 'm3D1v', 'Question_62XbhBvJ8NUSnApgDL94', 'midnight'], [2023, 10, 25, 0.22042341220423411, 177, 803, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'day'], [2023, 10, 25, 0.26679973386560213, 401, 1503, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'night'], [2023, 10, 26, 0.2391304347826087, 44, 184, 'm3D1v', 'Question_6RQj2gF3OeK5AmDvThUV', 'midnight'], [2023, 10, 26, 0.19617224880382775, 246, 1254, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'day'], [2023, 10, 26, 0.23579545454545456, 249, 1056, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'night'], [2023, 10, 27, 0.42857142857142855, 3, 7, 'y9W5d', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'midnight'], [2023, 10, 27, 0.17915904936014626, 98, 547, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 10, 27, 0.22786647314949202, 157, 689, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'night'], [2023, 10, 28, 0.25925925925925924, 7, 27, 'y9W5d', 'Question_xqlJkmRaP0otZcX4fK3W', 'midnight'], [2023, 10, 28, 0.24274406332453827, 184, 758, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf', 'day'], [2023, 10, 28, 0.19205298013245034, 116, 604, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'night'], [2023, 10, 29, 0.6153846153846154, 8, 13, 'y9W5d', 'Question_Ej5mBw9rsOUKkFycGvz2', 'midnight'], [2023, 10, 29, 0.3213367609254499, 250, 778, 'm3D1v', 'Question_Jr4Wz5jLqmN01KUwHa7g', 'day'], [2023, 10, 29, 0.2288135593220339, 189, 826, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'night'], [2023, 10, 30, 0.11382113821138211, 14, 123, 'm3D1v', 'Question_3MwAFlmNO8EKrpY5zjUd', 'midnight'], [2023, 10, 30, 0.28662420382165604, 270, 942, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'day'], [2023, 10, 30, 0.29812981298129815, 271, 909, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'night'], [2023, 10, 31, 0.1111111111111111, 2, 18, 't5V9e', 'Question_lU2wvHSZq7m43xiVroBc', 'midnight'], [2023, 10, 31, 0.21030042918454936, 196, 932, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'day'], [2023, 10, 31, 0.3037383177570093, 390, 1284, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 11, 1, 0.48148148148148145, 13, 27, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'midnight'], [2023, 11, 1, 0.1982421875, 203, 1024, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'day'], [2023, 11, 1, 0.20431990659661411, 350, 1713, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 11, 2, 0.4090909090909091, 9, 22, 'm3D1v', 'Question_bumGRTJ0c8p4v5D6eHZa', 'midnight'], [2023, 11, 2, 0.21954022988505748, 191, 870, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'day'], [2023, 11, 2, 0.2237871674491393, 286, 1278, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'night'], [2023, 11, 3, 0.24, 6, 25, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'midnight'], [2023, 11, 3, 0.21518987341772153, 170, 790, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'day'], [2023, 11, 3, 0.2058319039451115, 240, 1166, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'night'], [2023, 11, 4, 0.3125, 20, 64, 'm3D1v', 'Question_Ou3f2Wt9BqExm5DpN7Zk', 'midnight'], [2023, 11, 4, 0.18121546961325966, 164, 905, 'm3D1v', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'day'], [2023, 11, 4, 0.16911332941867294, 288, 1703, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'night'], [2023, 11, 5, 0.17647058823529413, 12, 68, 'b3C9s', 'Question_q7OpB2zCMmW9wS8uNt3H', 'midnight'], [2023, 11, 5, 0.21188630490956073, 164, 774, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 11, 5, 0.2230347349177331, 244, 1094, 'm3D1v', 'Question_h7pXNg80nJbw1C4kAPRm', 'night'], [2023, 11, 6, 0.2631578947368421, 20, 76, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'midnight'], [2023, 11, 6, 0.22259887005649717, 197, 885, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'day'], [2023, 11, 6, 0.28125, 288, 1024, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'night'], [2023, 11, 7, 0.2391304347826087, 11, 46, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'midnight'], [2023, 11, 7, 0.2723076923076923, 177, 650, 'm3D1v', 'Question_Ou3f2Wt9BqExm5DpN7Zk', 'day'], [2023, 11, 7, 0.26498422712933756, 336, 1268, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'night'], [2023, 11, 8, 0.11940298507462686, 8, 67, 'm3D1v', 'Question_x2Fy7rZ3SwYl9jMQkpOD', 'midnight'], [2023, 11, 8, 0.2288770053475936, 214, 935, 'm3D1v', 'Question_Jr4Wz5jLqmN01KUwHa7g', 'day'], [2023, 11, 8, 0.21428571428571427, 399, 1862, 'm3D1v', 'Question_fZrP3FJ4ebUogW9V7taS', 'night'], [2023, 11, 9, 0.13043478260869565, 15, 115, 'm3D1v', 'Question_Ej5mBw9rsOUKkFycGvz2', 'midnight'], [2023, 11, 9, 0.2154255319148936, 162, 752, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 11, 9, 0.23491773308957953, 257, 1094, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'night'], [2023, 11, 10, 0.3, 12, 40, 'y9W5d', 'Question_EhVPdmlB31M8WKGqL0wc', 'midnight'], [2023, 11, 10, 0.17688022284122562, 127, 718, 'm3D1v', 'Question_x2Fy7rZ3SwYl9jMQkpOD', 'day'], [2023, 11, 10, 0.17879948914431673, 140, 783, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'night'], [2023, 11, 11, 0.3333333333333333, 11, 33, 'y9W5d', 'Question_Az73sM0rHfWVKuc4X2kL', 'midnight'], [2023, 11, 11, 0.1553398058252427, 96, 618, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf', 'day'], [2023, 11, 11, 0.16191709844559585, 125, 772, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'night'], [2023, 11, 12, 0.18120805369127516, 27, 149, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'midnight'], [2023, 11, 12, 0.21875, 154, 704, 'm3D1v', 'Question_Ej5mBw9rsOUKkFycGvz2', 'day'], [2023, 11, 12, 0.20206766917293234, 215, 1064, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL', 'night'], [2023, 11, 13, 0.275, 11, 40, 'g7R2j', 'Question_X3wF8QlTyi4mZkDp9Kae', 'midnight'], [2023, 11, 13, 0.20517560073937152, 222, 1082, 'm3D1v', 'Question_UXqN1F7G3Sbldz02vZne', 'day'], [2023, 11, 13, 0.20826833073322934, 267, 1282, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'night'], [2023, 11, 14, 0.1590909090909091, 14, 88, 't5V9e', 'Question_oCjnFLbIs4Uxwek9rBpu', 'midnight'], [2023, 11, 14, 0.25158227848101267, 159, 632, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'day'], [2023, 11, 14, 0.2811023622047244, 357, 1270, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'night'], [2023, 11, 15, 0.375, 3, 8, 'y9W5d', 'Question_xqlJkmRaP0otZcX4fK3W', 'midnight'], [2023, 11, 15, 0.25380710659898476, 200, 788, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'day'], [2023, 11, 15, 0.2249034749034749, 466, 2072, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL', 'night'], [2023, 11, 16, 0.4722222222222222, 17, 36, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL', 'midnight'], [2023, 11, 16, 0.2121559633027523, 185, 872, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'day'], [2023, 11, 16, 0.2602739726027397, 304, 1168, 'm3D1v', 'Question_UXqN1F7G3Sbldz02vZne', 'night'], [2023, 11, 17, 0.12, 9, 75, 'y9W5d', 'Question_Az73sM0rHfWVKuc4X2kL', 'midnight'], [2023, 11, 17, 0.2851782363977486, 152, 533, 'm3D1v', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'day'], [2023, 11, 17, 0.2357142857142857, 231, 980, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf', 'night'], [2023, 11, 18, 0.17142857142857143, 6, 35, 'y9W5d', 'Question_62XbhBvJ8NUSnApgDL94', 'midnight'], [2023, 11, 18, 0.24556962025316456, 97, 395, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL', 'day'], [2023, 11, 18, 0.17407757805108798, 184, 1057, 'm3D1v', 'Question_62XbhBvJ8NUSnApgDL94', 'night'], [2023, 11, 19, 0.15789473684210525, 6, 38, 'g7R2j', 'Question_QRm48lXxzdP7Tn1WgNOf', 'midnight'], [2023, 11, 19, 0.25127334465195245, 148, 589, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'day'], [2023, 11, 19, 0.2462526766595289, 230, 934, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'night'], [2023, 11, 20, 0.23809523809523808, 10, 42, 'm3D1v', 'Question_bumGRTJ0c8p4v5D6eHZa', 'midnight'], [2023, 11, 20, 0.21151271753681392, 158, 747, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'day'], [2023, 11, 20, 0.24956217162872155, 285, 1142, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'night'], [2023, 11, 21, 0.225, 18, 80, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'midnight'], [2023, 11, 21, 0.25980392156862747, 265, 1020, 'm3D1v', 'Question_UXqN1F7G3Sbldz02vZne', 'day'], [2023, 11, 21, 0.22759103641456582, 325, 1428, 'm3D1v', 'Question_lU2wvHSZq7m43xiVroBc', 'night'], [2023, 11, 22, 0.10526315789473684, 6, 57, 'g7R2j', 'Question_xqlJkmRaP0otZcX4fK3W', 'midnight'], [2023, 11, 22, 0.24830699774266365, 220, 886, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'day'], [2023, 11, 22, 0.2832667047401485, 496, 1751, 'm3D1v', 'Question_Mh4CZIsrEfxkP1wXtOYV', 'night'], [2023, 11, 23, 0.2, 33, 165, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'midnight'], [2023, 11, 23, 0.25738798856053385, 270, 1049, 'm3D1v', 'Question_BW0ItEaymH3TkD6S15JF', 'day'], [2023, 11, 23, 0.2127215849843587, 408, 1918, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 11, 24, 0.423728813559322, 25, 59, 'g7R2j', 'Question_xqlJkmRaP0otZcX4fK3W', 'midnight'], [2023, 11, 24, 0.27502750275027504, 250, 909, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 11, 24, 0.25502742230347347, 279, 1094, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 11, 25, 0.11320754716981132, 6, 53, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'midnight'], [2023, 11, 25, 0.31962025316455694, 303, 948, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL', 'day'], [2023, 11, 25, 0.21603563474387527, 194, 898, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 11, 26, 0.27586206896551724, 8, 29, 'm3D1v', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'midnight'], [2023, 11, 26, 0.3035971223021583, 211, 695, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 11, 26, 0.2840095465393795, 357, 1257, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'night'], [2023, 11, 27, 0.16666666666666666, 8, 48, 'm3D1v', 'Question_hZ5wXofebmTlzKB1jNcP', 'midnight'], [2023, 11, 27, 0.23661071143085532, 296, 1251, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL', 'day'], [2023, 11, 27, 0.28641171684296174, 352, 1229, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL', 'night'], [2023, 11, 28, 0.1927710843373494, 16, 83, 'y9W5d', 'Question_q7OpB2zCMmW9wS8uNt3H', 'midnight'], [2023, 11, 28, 0.30634146341463414, 314, 1025, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'day'], [2023, 11, 28, 0.23897911832946636, 206, 862, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 11, 29, 0.3148148148148148, 17, 54, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'midnight'], [2023, 11, 29, 0.31226765799256506, 168, 538, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'day'], [2023, 11, 29, 0.3012524719841793, 457, 1517, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf', 'night'], [2023, 11, 30, 0.5789473684210527, 11, 19, 'y9W5d', 'Question_X3wF8QlTyi4mZkDp9Kae', 'midnight'], [2023, 11, 30, 0.23024830699774265, 204, 886, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 11, 30, 0.25995449374288965, 457, 1758, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 1, 0.38333333333333336, 23, 60, 'm3D1v', 'Question_62XbhBvJ8NUSnApgDL94', 'midnight'], [2023, 12, 1, 0.3159420289855073, 218, 690, 'm3D1v', 'Question_bumGRTJ0c8p4v5D6eHZa', 'day'], [2023, 12, 1, 0.2751247327156094, 386, 1403, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 2, 0.32954545454545453, 29, 88, 'y9W5d', 'Question_x2Fy7rZ3SwYl9jMQkpOD', 'midnight'], [2023, 12, 2, 0.24635922330097088, 203, 824, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 12, 2, 0.32275132275132273, 305, 945, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 3, 0.5813953488372093, 25, 43, 'g7R2j', 'Question_x2Fy7rZ3SwYl9jMQkpOD', 'midnight'], [2023, 12, 3, 0.30605738575983, 288, 941, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 12, 3, 0.26452905811623245, 264, 998, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 4, 0.3382352941176471, 23, 68, 'y9W5d', 'Question_FNg8X9v5zcbB1tQrxHR3', 'midnight'], [2023, 12, 4, 0.29020556227327693, 240, 827, 'm3D1v', 'Question_oCjnFLbIs4Uxwek9rBpu', 'day'], [2023, 12, 4, 0.24021739130434783, 221, 920, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 5, 0.038461538461538464, 1, 26, 'y9W5d', 'Question_oCjnFLbIs4Uxwek9rBpu', 'midnight'], [2023, 12, 5, 0.4038128249566724, 466, 1154, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 12, 5, 0.2934682612695492, 319, 1087, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'night'], [2023, 12, 6, 0.27, 27, 100, 'r8S3g', 'Question_5fgqjSBwTPG7KUV3it6O', 'midnight'], [2023, 12, 6, 0.30072173215717724, 375, 1247, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 12, 6, 0.260625, 417, 1600, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 7, 0.185, 37, 200, 'm3D1v', 'Question_Ej5mBw9rsOUKkFycGvz2', 'midnight'], [2023, 12, 7, 0.2916666666666667, 140, 480, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'day'], [2023, 12, 7, 0.26519916142557654, 253, 954, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 8, 0.09090909090909091, 8, 88, 'r8S3g', 'Question_BW0ItEaymH3TkD6S15JF', 'midnight'], [2023, 12, 8, 0.3168, 198, 625, 'm3D1v', 'Question_X3wF8QlTyi4mZkDp9Kae', 'day'], [2023, 12, 8, 0.2901484480431849, 215, 741, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 9, 0.7857142857142857, 11, 14, 'g7R2j', 'Question_oCjnFLbIs4Uxwek9rBpu', 'midnight'], [2023, 12, 9, 0.3637795275590551, 231, 635, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 12, 9, 0.2962962962962963, 216, 729, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'night'], [2023, 12, 10, 0.10204081632653061, 5, 49, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'midnight'], [2023, 12, 10, 0.24347826086956523, 84, 345, 'g7R2j', 'Question_xqlJkmRaP0otZcX4fK3W', 'day'], [2023, 12, 10, 0.26773455377574373, 117, 437, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 11, 0.24242424242424243, 16, 66, 'y9W5d', 'Question_EhVPdmlB31M8WKGqL0wc', 'midnight'], [2023, 12, 11, 0.19166666666666668, 69, 360, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'day'], [2023, 12, 11, 0.2583826429980276, 131, 507, 'y9W5d', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 12, 1.0, 1, 1, 'y9W5d', 'Question_EhVPdmlB31M8WKGqL0wc', 'midnight'], [2023, 12, 12, 0.25477707006369427, 120, 471, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'day'], [2023, 12, 12, 0.36894075403949733, 411, 1114, 'm3D1v', 'Question_Az73sM0rHfWVKuc4X2kL', 'night'], [2023, 12, 13, 0.5625, 27, 48, 'y9W5d', 'Question_EhVPdmlB31M8WKGqL0wc', 'midnight'], [2023, 12, 13, 0.23987034035656402, 148, 617, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 12, 13, 0.32582938388625593, 550, 1688, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 14, 0.14166666666666666, 17, 120, 'm3D1v', 'Question_x2Fy7rZ3SwYl9jMQkpOD', 'midnight'], [2023, 12, 14, 0.41770186335403725, 269, 644, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'day'], [2023, 12, 14, 0.23582766439909297, 208, 882, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 15, 0.047619047619047616, 2, 42, 'y9W5d', 'Question_FNg8X9v5zcbB1tQrxHR3', 'midnight'], [2023, 12, 15, 0.17412935323383086, 70, 402, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'day'], [2023, 12, 15, 0.3549432739059968, 219, 617, 'y9W5d', 'Question_X3wF8QlTyi4mZkDp9Kae', 'night'], [2023, 12, 16, 0, 0, 0, 'None', 'None', 'midnight'], [2023, 12, 16, 0.30718336483931946, 325, 1058, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'day'], [2023, 12, 16, 0.21483622350674375, 223, 1038, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 17, 1.0, 1, 1, 'b3C9s', 'Question_hZ5wXofebmTlzKB1jNcP', 'midnight'], [2023, 12, 17, 0.35545023696682465, 75, 211, 'g7R2j', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'day'], [2023, 12, 17, 0.4160756501182033, 176, 423, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 18, 0.16666666666666666, 1, 6, 'b3C9s', 'Question_hZ5wXofebmTlzKB1jNcP', 'midnight'], [2023, 12, 18, 0.2892857142857143, 81, 280, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'day'], [2023, 12, 18, 0.3346774193548387, 166, 496, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'night'], [2023, 12, 19, 0.4358974358974359, 17, 39, 'b3C9s', 'Question_hZ5wXofebmTlzKB1jNcP', 'midnight'], [2023, 12, 19, 0.40902255639097745, 272, 665, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 12, 19, 0.3056768558951965, 210, 687, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'night'], [2023, 12, 20, 1.0, 6, 6, 'b3C9s', 'Question_Ej5mBw9rsOUKkFycGvz2', 'midnight'], [2023, 12, 20, 0.3567708333333333, 274, 768, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'day'], [2023, 12, 20, 0.37718120805369126, 281, 745, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'night'], [2023, 12, 21, 0.631578947368421, 12, 19, 'b3C9s', 'Question_Mh4CZIsrEfxkP1wXtOYV', 'midnight'], [2023, 12, 21, 0.3443223443223443, 188, 546, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'day'], [2023, 12, 21, 0.3586337760910816, 189, 527, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 22, 0.0, 0, 13, 'y9W5d', 'Question_Az73sM0rHfWVKuc4X2kL', 'midnight'], [2023, 12, 22, 0.23694779116465864, 59, 249, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'day'], [2023, 12, 22, 0.29161290322580646, 226, 775, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'night'], [2023, 12, 23, 0.5238095238095238, 11, 21, 'g7R2j', 'Question_FNg8X9v5zcbB1tQrxHR3', 'midnight'], [2023, 12, 23, 0.34205607476635513, 183, 535, 'm3D1v', 'Question_X3wF8QlTyi4mZkDp9Kae', 'day'], [2023, 12, 23, 0.2536443148688047, 174, 686, 'y9W5d', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 24, 0.4, 2, 5, 'y9W5d', 'Question_Az73sM0rHfWVKuc4X2kL', 'midnight'], [2023, 12, 24, 0.38596491228070173, 88, 228, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'day'], [2023, 12, 24, 0.32264957264957267, 151, 468, 'm3D1v', 'Question_EhVPdmlB31M8WKGqL0wc', 'night'], [2023, 12, 25, 0.375, 12, 32, 'g7R2j', 'Question_pVKXjZn0BkSwYcsa7C31', 'midnight'], [2023, 12, 25, 0.2788104089219331, 75, 269, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2023, 12, 25, 0.3734513274336283, 211, 565, 'y9W5d', 'Question_5fgqjSBwTPG7KUV3it6O', 'night'], [2023, 12, 26, 1.0, 1, 1, 'b3C9s', 'Question_hZ5wXofebmTlzKB1jNcP', 'midnight'], [2023, 12, 26, 0.2925764192139738, 67, 229, 'y9W5d', 'Question_pVKXjZn0BkSwYcsa7C31', 'day'], [2023, 12, 26, 0.43781942078364566, 257, 587, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 27, 0.2, 1, 5, 'b3C9s', 'Question_hZ5wXofebmTlzKB1jNcP', 'midnight'], [2023, 12, 27, 0.3054892601431981, 128, 419, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'day'], [2023, 12, 27, 0.4943502824858757, 175, 354, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 28, 0.358974358974359, 14, 39, 'g7R2j', 'Question_xqlJkmRaP0otZcX4fK3W', 'midnight'], [2023, 12, 28, 0.38875305623471884, 159, 409, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf', 'day'], [2023, 12, 28, 0.4099526066350711, 173, 422, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'night'], [2023, 12, 29, 0.5, 3, 6, 'm3D1v', 'Question_oCjnFLbIs4Uxwek9rBpu', 'midnight'], [2023, 12, 29, 0.483974358974359, 151, 312, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'day'], [2023, 12, 29, 0.3825136612021858, 140, 366, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 30, 0.0, 0, 3, 'g7R2j', 'Question_5fgqjSBwTPG7KUV3it6O', 'midnight'], [2023, 12, 30, 0.41368584758942456, 266, 643, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'day'], [2023, 12, 30, 0.41420118343195267, 350, 845, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2023, 12, 31, 0.7777777777777778, 14, 18, 't5V9e', 'Question_h7pXNg80nJbw1C4kAPRm', 'midnight'], [2023, 12, 31, 0.5681341719077568, 271, 477, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'day'], [2023, 12, 31, 0.3949579831932773, 94, 238, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2024, 1, 1, 0.0, 0, 12, 'm3D1v', 'Question_oCjnFLbIs4Uxwek9rBpu', 'midnight'], [2024, 1, 1, 0.3974025974025974, 153, 385, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'day'], [2024, 1, 1, 0.4872611464968153, 153, 314, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'night'], [2024, 1, 2, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 2, 0.3146067415730337, 56, 178, 'm3D1v', 'Question_hZ5wXofebmTlzKB1jNcP', 'day'], [2024, 1, 2, 0.4393241167434716, 286, 651, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'night'], [2024, 1, 3, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 3, 0.6276595744680851, 59, 94, 'g7R2j', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'day'], [2024, 1, 3, 0.36088709677419356, 179, 496, 'm3D1v', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'night'], [2024, 1, 4, 0.23529411764705882, 4, 17, 'm3D1v', 'Question_FNg8X9v5zcbB1tQrxHR3', 'midnight'], [2024, 1, 4, 0.5526315789473685, 21, 38, 'm3D1v', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2024, 1, 4, 0.5040650406504065, 62, 123, 'm3D1v', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2024, 1, 5, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 5, 0.8823529411764706, 15, 17, 'm3D1v', 'Question_pVKXjZn0BkSwYcsa7C31', 'day'], [2024, 1, 5, 0.4075342465753425, 119, 292, 'm3D1v', 'Question_Mh4CZIsrEfxkP1wXtOYV', 'night'], [2024, 1, 6, 0.0, 0, 14, 'b3C9s', 'Question_hZ5wXofebmTlzKB1jNcP', 'midnight'], [2024, 1, 6, 0.6923076923076923, 63, 91, 'y9W5d', 'Question_lU2wvHSZq7m43xiVroBc', 'day'], [2024, 1, 6, 0.5562913907284768, 84, 151, 'y9W5d', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'night'], [2024, 1, 7, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 7, 0.5441176470588235, 37, 68, 'g7R2j', 'Question_hZ5wXofebmTlzKB1jNcP', 'day'], [2024, 1, 7, 0.6097560975609756, 25, 41, 'g7R2j', 'Question_X3wF8QlTyi4mZkDp9Kae', 'night'], [2024, 1, 8, 0.4166666666666667, 10, 24, 'g7R2j', 'Question_3MwAFlmNO8EKrpY5zjUd', 'midnight'], [2024, 1, 8, 0.6097560975609756, 25, 41, 'g7R2j', 'Question_hZ5wXofebmTlzKB1jNcP', 'day'], [2024, 1, 8, 0.8360655737704918, 102, 122, 'm3D1v', 'Question_NixCn84GdK2tySa5rB1V', 'night'], [2024, 1, 9, 1.0, 1, 1, 'y9W5d', 'Question_Ej5mBw9rsOUKkFycGvz2', 'midnight'], [2024, 1, 9, 0.7, 7, 10, 'm3D1v', 'Question_QRm48lXxzdP7Tn1WgNOf', 'day'], [2024, 1, 9, 0.5232558139534884, 45, 86, 'y9W5d', 'Question_FNg8X9v5zcbB1tQrxHR3', 'night'], [2024, 1, 10, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 10, 0.4057971014492754, 84, 207, 'm3D1v', 'Question_X3wF8QlTyi4mZkDp9Kae', 'day'], [2024, 1, 10, 0.5197368421052632, 158, 304, 'm3D1v', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'night'], [2024, 1, 11, 0.8888888888888888, 16, 18, 'g7R2j', 'Question_bumGRTJ0c8p4v5D6eHZa', 'midnight'], [2024, 1, 11, 1.0, 3, 3, 'g7R2j', 'Question_lU2wvHSZq7m43xiVroBc', 'day'], [2024, 1, 11, 0, 0, 0, 'None', 'None', 'night'], [2024, 1, 12, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 12, 0, 0, 0, 'None', 'None', 'day'], [2024, 1, 12, 0.38461538461538464, 5, 13, 'y9W5d', 'Question_Mh4CZIsrEfxkP1wXtOYV', 'night'], [2024, 1, 13, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 13, 0.8846153846153846, 23, 26, 'y9W5d', 'Question_Mh4CZIsrEfxkP1wXtOYV', 'day'], [2024, 1, 13, 0, 0, 0, 'None', 'None', 'night'], [2024, 1, 14, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 14, 0.4519230769230769, 47, 104, 'm3D1v', 'Question_BW0ItEaymH3TkD6S15JF', 'day'], [2024, 1, 14, 0.4460093896713615, 95, 213, 'm3D1v', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'night'], [2024, 1, 15, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 15, 0.6521739130434783, 30, 46, 'y9W5d', 'Question_xqlJkmRaP0otZcX4fK3W', 'day'], [2024, 1, 15, 0, 0, 0, 'None', 'None', 'night'], [2024, 1, 16, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 16, 0.7391304347826086, 17, 23, 'b3C9s', 'Question_X3wF8QlTyi4mZkDp9Kae', 'day'], [2024, 1, 16, 0.0, 0, 7, 'g7R2j', 'Question_xqlJkmRaP0otZcX4fK3W', 'night'], [2024, 1, 20, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 20, 0.3333333333333333, 2, 6, 'g7R2j', 'Question_X3wF8QlTyi4mZkDp9Kae', 'day'], [2024, 1, 20, 0, 0, 0, 'None', 'None', 'night'], [2024, 1, 21, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 21, 0, 0, 0, 'None', 'None', 'day'], [2024, 1, 21, 0.8888888888888888, 8, 9, 'm3D1v', 'Question_h7pXNg80nJbw1C4kAPRm', 'night'], [2024, 1, 22, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 22, 0.2, 1, 5, 'r8S3g', 'Question_VgKw8PjY1FR6cm2QI9XW', 'day'], [2024, 1, 22, 0, 0, 0, 'None', 'None', 'night'], [2024, 1, 23, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 23, 0, 0, 0, 'None', 'None', 'day'], [2024, 1, 23, 1.0, 1, 1, 't5V9e', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'night'], [2024, 1, 25, 0, 0, 0, 'None', 'None', 'midnight'], [2024, 1, 25, 1.0, 3, 3, 'g7R2j', 'Question_5fgqjSBwTPG7KUV3it6O', 'day'], [2024, 1, 25, 0, 0, 0, 'None', 'None', 'night']]

        }
    }, 
    mounted() {
        this.draw_part_2();
    },
    methods: {
        draw_part_2() {
            const draw = () => {
            this.data_parse();
            const mapping = {'midnight': '凌晨', 'day': '白天', 'night': '夜晚'};
            var chartDom = document.getElementById('secondpart');
            // console.log(chartDom)
            var myChart = echarts.init(chartDom);
            var option;
            // const minVal = this.data.reduce((min, val) => Math.min(min, val[1]), Infinity) * 100;
            // const maxVal = this.data.reduce((max, val) => Math.max(max, val[1]), -Infinity) * 100;
            // console.log("in function draw_part_2(), ", minVal, maxVal);
            // function getColorForValue(value, minValue, maxValue) {
            //     const ratio = (value - minValue) / (maxValue - minValue);
            //     const hue = ratio * 120; // 0 (red) to 120 (green) in HSL color space
            //     return `hsl(${hue}, 100%, 50%)`;
            // }
            let data1 = this.data.filter((_, index) => index % 3 === 0);
            let data2 = this.data.filter((_, index) => index % 3 === 1);
            let data3 = this.data.filter((_, index) => index % 3 === 2);
            // console.log(data1);
            option = {
            animation: false,
            legend: {
                data: ['凌晨', '白天', '夜晚']
            },
            tooltip: {
                show: true,
                formatter: function (param) {
                    const info = param.data;
                    return `日期: ${info[0]}<br>
                            时间段: ${mapping[info[6]]}<br>
                            本时间段通过率: ${info[1]}<br>
                            本时间段总通过次数: ${info[2]}<br>
                            本时间段总提交次数: ${info[3]}<br>
                            本时间段热门知识点: ${info[4]}<br>
                            本时间段热门题目: ${info[5]}<br>        
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
                    name: '凌晨',
                    type: 'scatter',
                    itemStyle: {
                        normal: {
                        opacity: 0.8
                        // color: function (param) {
                        //     console.log("Pass rate is : ", param.value[1]);
                        //         return getColorForValue(param.value[1] * 100, minVal, maxVal);
                        //     }
                        }
                    },
                    symbolSize: function (val) {
                        return Math.sqrt(val[3] / 50) * 20;
                    },
                    data: data1
                },
                {
                    name: '白天',
                    type: 'scatter',
                    itemStyle: {
                        normal: {
                        opacity: 0.8
                        }
                    },
                    symbolSize: function (val) {
                        return Math.sqrt(val[3] / 50) * 10;
                    },
                    data: data2
                },
                {
                    name: '夜晚',
                    type: 'scatter',
                    itemStyle: {
                        normal: {
                        opacity: 0.8
                        }
                    },
                    symbolSize: function (val) {
                        return Math.sqrt(val[3] / 50) * 10;
                    },
                    data: data3
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
            // console.log(this.data);
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>