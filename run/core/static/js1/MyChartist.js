function drawChart(x,y) {
    //ct-visits
    Chartist.Line('#ct-visits', {
     labels: [{%- for item in x -%} '{{item|tojson|safe}}', {%- endfor -%}],
     series: [[],[{%- for item in y- %} {{item|tojson|safe}}, {%- endfor -%} ]]
    }, {
     showPoint: true,
     fullWidth: true,
     plugins: [
    Chartist.plugins.tooltip()
    ],
     axisY: {
         labelInterpolationFnc: function (value) {
             return '$'+(value);
         }
     },
     showArea: true
    });
}