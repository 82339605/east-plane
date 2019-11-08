var padDate = function (value) {
    return value<10 ? '0'+ value:value;
}
// var send = new Vue({
//     el:'.send',
//     data:{
//         background: 'red'
//     }
// })
// var get = new Vue({
//     el:'.get',
//     data:{
//     background: 'red'
//     }
// })
var app = new Vue({
    el:'.form-data',
    data:{
        name: 'tickets',
        date: new Date(),
        sbackground:'rgba(255,255,255)',
        gbackground:'rgba(255,0,0,0.5)',
        kbackground:'black',
        tbackground:'black',
        jbackground:'rgba(255,0,0,0.5)',
        lbackground:'rgba(255,255,255)',
        time: new Date(),
        destination:'get-people',
        nav:'buytickets',
        color:'white',
        plane:'get-in',
        state:'time-schedule',
        according:'num-plane'
    },
    computed:{
      dt:function () {
          var dt = new Date()
          y = padDate(dt.getFullYear())
          m = padDate(dt.getMonth()+1)
          d = padDate(dt.getDate())
          return y+'-'+m+'-'+d
      }
    },
    methods:{
        getcolor:function(){
            this.jbackground = 'rgba(255,0,0,0.5)'
            this.lbackground = 'rgba(255,255,255)'
            this.plane = 'get-in'
            this.according = 'num-plane'
        },
        leavecolor:function(){
             this.jbackground = 'rgba(255,255,255)'
            this.lbackground = 'rgba(255,0,0,0.5)'
            this.plane = 'leave-in'
            this.according = 'begin-place'
        },
        change:function () {
            return this.name = 'get_tickets'
        },
        first:function () {
            return this.name = 'tickets'
        },
        hotel:function () {
            return this.name = 'hotel'
        },
        shuttle:function () {
            return this.name = 'shuttle'
        },
        change_color:function () {
            this.sbackground = 'rgba(255,0,0,0.5)'
            this.gbackground = 'rgba(255,255,255)'
            this.destination = 'send-people'
            this.kbackground = 'red'
            this.tbackground = 'black'
            this.state = 'plane-dymanic'
        },
        changecolor:function () {
            this.sbackground = 'rgba(255,255,255)'
            this.gbackground = 'rgba(255,0,0,0.5)'
            this.destination = 'get-people'
            this.kbackground = 'black'
            this.tbackground = 'red'
            this.state = 'time-schedule'
        },
        buy:function () {
            this.nav='buytickets'
        },
        Dynamic:function () {
            this.nav = 'dynamic'
        },
        east:function () {
            this.nav = 'east'
        }
    },
    filters:{
        formatDate:function (value) {
            var date = new Date(value);
            var year = date.getFullYear();
            var month = padDate(date.getMonth()+1);
            var day = padDate(date.getDate());
            var hours = padDate(date.getHours());
            var minutes = padDate(date.getMinutes());
            var seconds = padDate(date.getSeconds());
            return year+'-'+month+'-'+day+'-'+hours+':'+minutes+':'+seconds;
        },
        changeTime:function (value) {
              var time = new Date(value)
              var hour = padDate(time.getHours())
              var minute = padDate(time.getMinutes())
              var second = padDate(time.getSeconds())
              return hour+':'+minute+':'+second

        }
    },
    mounted:function () {
        var _this = this;
        this.timer = setInterva`
        l(function () {
            _this.date = new Date();
            _this.time = new Date();
        },1000)
    },
    beforeDestroy:function () {
        if(this.timer){
            clearInterval(this.timer);
        }
    }
})
