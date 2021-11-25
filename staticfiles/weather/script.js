const App1 = {
    data(){
        return {
            api_key:'98f4b08fcfbf58bc37ca21d1ad8614b6',
            url_base: 'https://api.openweathermap.org/data/2.5/',
            query:'',
            weather: {} 
        }
    },
    methods:{
        fetchWeather(e){
            if(e.key == 'Enter'){
              fetch(`${this.url_base}weather?q=${this.query}&units=metric&APPID=${this.api_key}`).then(res => {
                return res.json();
              }).then(this.setResults)
            }
          },
          setResults(results){
            this.weather = results
          },
          dateBuilder(){
            let d = new Date()
            let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]
            let days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
      
            let day = days[d.getDay()]
            let date = d.getDate()
            let month = months[d.getMonth()]
            let year = d.getFullYear()
            
            return `${day} ${date} ${month} ${year} `
          }
    }
}
Vue.createApp(App1).mount("#app")