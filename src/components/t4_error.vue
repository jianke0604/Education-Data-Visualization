<template>
    <div id="error" style="height: 600px; width: 100%;"></div>
</template>

<script>
import * as echarts from 'echarts'

export default {
    name: 'Error',
    data() {
        return {
            data: [[74.4186046511628, 28.874494738065216], [65.814696485623, 27.68122194086423], [57.9646017699115, 29.146649595407265], [53.99188092016238, 30.47734030674378], [76.13227893601724, 21.520008686202186], [68.796992481203, 22.880000869108407], [56.475300400534046, 27.245954504829196], [58.417085427135675, 26.152289417842052], [59.23295454545454, 25.223317417722217], [55.71808510638297, 26.533967493531186], [58.34428383705651, 24.0290831748382], [49.48905109489051, 28.25557018983932], [65.60574948665298, 21.299980860121487], [56.417112299465245, 24.603856407279526], [62.96743063932448, 21.73689279724407], [51.71339563862928, 26.41491754161945], [58.95806861499364, 22.756445384691318], [55.7163531114327, 23.976190458019914], [49.11971830985916, 27.012144691397438], [52.18002812939522, 25.0646947156864], [49.473684210526315, 26.353342282559062], [48.67256637168141, 25.1303378634597], [51.223241590214066, 23.537983028207535], [43.609022556390975, 27.55588232982949], [47.22222222222222, 25.405400948595275], [49.13112164296998, 23.80780673713922], [46.1890243902439, 25.069557859715793], [43.03571428571429, 26.43828589390246], [44.81546572934973, 24.136141328641692], [33.18872017353579, 30.983011184050966], [37.634408602150536, 24.82967447582668], [36.400817995910025, 24.760617563757478], [34.93449781659388, 25.107754842752804], [36.41851106639839, 23.762597565755584], [37.903225806451616, 22.40998420627916], [35.13513513513514, 24.074220165096886], [32.03463203463203, 24.863793985540493], [26.717557251908396, 23.4415684495646]],
            q: ['Question_5fgqjSBwTPG7KUV3it6O', 'Question_n2BTxIGw1Mc3Zo6RLdUe', 'Question_YWXHr4G6Cl7bEm9iF2kQ', 'Question_FNg8X9v5zcbB1tQrxHR3', 'Question_q7OpB2zCMmW9wS8uNt3H', 'Question_3MwAFlmNO8EKrpY5zjUd', 'Question_EhVPdmlB31M8WKGqL0wc', 'Question_x2Fy7rZ3SwYl9jMQkpOD', 'Question_xqlJkmRaP0otZcX4fK3W', 'Question_Az73sM0rHfWVKuc4X2kL', 'Question_BW0ItEaymH3TkD6S15JF', 'Question_X3wF8QlTyi4mZkDp9Kae', 'Question_3oPyUzDmQtcMfLpGZ0jW', 'Question_h7pXNg80nJbw1C4kAPRm', 'Question_fZrP3FJ4ebUogW9V7taS', 'Question_62XbhBvJ8NUSnApgDL94', 'Question_VgKw8PjY1FR6cm2QI9XW', 'Question_pVKXjZn0BkSwYcsa7C31', 'Question_oCjnFLbIs4Uxwek9rBpu', 'Question_QRm48lXxzdP7Tn1WgNOf', 'Question_s6VmP1G4UbEQWRYHK9Fd', 'Question_Mh4CZIsrEfxkP1wXtOYV', 'Question_TmKaGvfNoXYq4FZ2JrBu', 'Question_ZTbD7mxr2OUp8Fz6iNjy', 'Question_Jr4Wz5jLqmN01KUwHa7g', 'Question_lU2wvHSZq7m43xiVroBc', 'Question_Ej5mBw9rsOUKkFycGvz2', 'Question_bumGRTJ0c8p4v5D6eHZa', 'Question_tgOjrpZLw4RdVzQx85h6', 'Question_hZ5wXofebmTlzKB1jNcP', 'Question_UXqN1F7G3Sbldz02vZne', 'Question_7NJzCXUPcvQF4Mkfh9Wr', 'Question_NixCn84GdK2tySa5rB1V', 'Question_4nHcauCQ0Y6Pm8DgKlLo', 'Question_x2L7AqbMuTjCwPFy6vNr', 'Question_6RQj2gF3OeK5AmDvThUV', 'Question_Ou3f2Wt9BqExm5DpN7Zk', 'Question_rvB9mVE6Kbd8jAY4NwPx']
        }
    },
    mounted() {
        // this.data_parse();
        this.draw_part_2();
    },
    methods: {
        draw_part_2() {
            const draw = () => {
                        var chartDom = document.getElementById('error');
                        var myChart = echarts.init(chartDom);
                        var option;
                        var q = this.q;

                        option = {
                            xAxis: {},
                            yAxis: {},
                            series: [
                                {
                                symbolSize: 20,
                                data: this.data,
                                type: 'scatter'
                                }
                            ],
                            tooltip: {
                                trigger: 'item',
                                formatter: function (params) {
                                    return q[params.dataIndex];
                                }
                            }
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
            fetch('../../data/q2_zoom_chart.json')
                .then(response => response.json())
                .then(dataload => {
                    console.log("in fetch: ", dataload);
                    this.data = dataload;
                    for (let i = 0; i < this.data.length; i++) {
                        const year = this.data[i][0];
                        const month = this.data[i][1];
                        const day = this.data[i][2];
                        this.data[i].splice(0, 3, `${year}-${month}-${day}`);
                        // this.data[i][0] = new Date(this.data[i][0]);
                    }
                })
                .catch(error => console.error('Error loading data', error));
            
            console.log("in data parse function, ", this.data);
        }
    }

}
</script>

<style >

</style>