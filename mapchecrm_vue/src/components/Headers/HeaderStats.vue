<template>
  <!-- Header -->
  <div class="relative md:pt-32 pb-32 pt-12">
    <div
          class="absolute top-0 w-full h-full bg-no-repeat bg-full bg-pink"
          :style="`background-image: url('${registerBg2}');`"
        >
        </div>
    <div class="px-4 md:px-10 mx-auto w-full">
      <div>
        <!-- Card stats -->
        <div class="flex flex-wrap">
          <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
            <card-stats
              statSubtitle="SEARCHES"
              :statTitle="`${this.searchesstatTitle}`"
              :statArrow="`${this.searchesstatArrow}`"
              :statPercent="`${this.searchesstatPercent}`"
              :statPercentColor="`${this.searchesstatPercentColor}`"
              statDescripiron="Since last month"
              statIconName="far fa-chart-bar"
              statIconColor="bg-red-500"
            />
          </div>
          <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
            <card-stats
              statSubtitle="NEW USERS"
              :statTitle="`${this.userstatTitle}`"
              :statArrow="`${this.userstatArrow}`"
              :statPercent="`${this.userstatPercent}`"
              :statPercentColor="`${this.userstatPercentColor}`"              statDescripiron="Since last week"
              statIconName="fas fa-chart-pie"
              statIconColor="bg-orange-500"
            />
          </div>
          <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
            <card-stats
              statSubtitle="NEW LEADS"
              statTitle="924"
              statArrow="down"
              statPercent="1.10"
              statPercentColor="text-orange-500"
              statDescripiron="Since yesterday"
              statIconName="fas fa-users"
              statIconColor="bg-pink-500"
            />
          </div>
          <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
            <card-stats
              statSubtitle="PERFORMANCE"
              statTitle="49,65%"
              statArrow="up"
              statPercent="12"
              statPercentColor="text-emerald-500"
              statDescripiron="Since last month"
              statIconName="fas fa-percent"
              statIconColor="bg-emerald-500"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CardStats from "@/components/Cards/CardStats.vue"
import registerBg2 from "@/assets/img/register_bg_2.png"
import moment from 'moment'

export default {
  name: 'HeaderStats',

  mounted() {
    this.getSearches()
  },
  computed: {
    percentage() {
      return (this.searches.length / this.totalSearches * 100).toFixed(1)
    },
  },
  components: {
    CardStats,
  },
  data() {
    return {
      registerBg2,
      searches: [],
      totalSearches: 1000,
      thisMonth: 0,
      previousMonth: 0,
      thisSevenDays: 0,
      this2Weeks: 0,
      searchesstatTitle: 0,
      searchesstatArrow: '',
      searchesstatPercent: 0,
      searchesstatPercentColor: '',
      userstatTitle: 0,
      userstatArrow: '',
      userstatPercent: 0,
      userstatPercentColor: '',
      numberValue: '',
      numArray: [],
      numberValue2: '',
      numArray2: []
    };
  },

  methods: {
    async getSearches() {
      this.$store.commit('setIsLoading', true)

      axios
        .get('/mapche-api/v1/search/')
        .then(response => {
          this.searches = response.data
          this.thisMonth = 0
          this.previousMonth = 0
          this.thisSevenDays = 0
          this.this2Weeks = 0
          for (var i = 0; i < response.data.length; i++) {
            const searchData = response.data[i].created_at
            const today = moment()
            const lastSevenDays = moment().subtract(7, 'days')
            const last2Weeks = moment().subtract(14, 'days')
            const lastThirtyDays = moment().subtract(30, 'days')
            const lastSixtyDays = moment().subtract(60, 'days')
            //New Users
            const isValidSevenDays = moment(searchData).isBetween(lastSevenDays, today, 'day', '[]')
            console.log(isValidSevenDays)
            const isValid2Weeks = moment(searchData).isBetween(last2Weeks, lastSevenDays, 'day', '[]')
            //New Searches
            const isValidThirtyDays = moment(searchData).isBetween(lastThirtyDays, today, 'day', '[]')
            const isValidSixtyDays = moment(searchData).isBetween(lastSixtyDays, lastThirtyDays, 'day', '[]')

            if (isValidThirtyDays) {
              this.thisMonth = (this.thisMonth + 1)
            } 
            if (isValidSixtyDays) {
              this.previousMonth = (this.previousMonth + 1)
            }
            if (isValidSevenDays) {
              //Unique New Users
              this.numberValue = response.data[i].infoIp
              if (this.numberValue != null) {
                this.numArray.push(this.numberValue)
                this.numArray = [...new Set(this.numArray)]
               }
            }
            if (isValid2Weeks) {
              //Unique New Users
              this.numberValue2 = response.data[i].infoIp
              if (this.numberValue2 != null) {
                this.numArray2.push(this.numberValue2)
                this.numArray2 = [...new Set(this.numArray2)]
               }
            }
          } 
          this.thisSevenDays = (this.numArray)
          console.log(this.thisSevenDays.length)
          this.this2Weeks = (this.numArray2)
          console.log(this.this2Weeks.length)
          
          // Searches
          if (this.previousMonth == 0 && this.thisMonth != 0) {
            var searchmom = ((this.thisMonth)/this.thisMonth * 100)      
          } else if (this.thisMonth == 0 && this.previousMonth !=0) {
            var searchmom = ((this.thisMonth - this.previousMonth)/this.previousMonth * 100)      
          } else if (this.thisMonth == 0 && this.previousMonth == 0) {
            var searchmom = 0
          } else {
            var searchmom = ((this.thisMonth - this.previousMonth)/this.previousMonth * 100)      
          }

          //Users
          if (this.this2Weeks.length == 0 && this.thisSevenDays.length != 0) {
            var usermom = ((this.thisSevenDays.length)/this.thisSevenDays.length * 100)      
          } else if (this.thisSevenDays.length == 0 && this.this2Weeks.length !=0) {
            var usermom = ((this.thisSevenDays.length - this.this2Weeks.length)/this.this2Weeks.length * 100)      
          } else if (this.thisSevenDays.length == 0 && this.this2Weeks.length == 0) {
            var usermom = 0
          } else {
            var usermom = ((this.thisSevenDays.length - this.this2Weeks.length)/this.this2Weeks.length * 100)      
          }

          // Search stats header
          if (searchmom >= 0) {
            this.searchesstatTitle = this.thisMonth
            //total searches in db this.searches.length
            this.searchesstatArrow = 'up'
            this.searchesstatPercent = searchmom
            this.searchesstatPercentColor = "text-emerald-500"   
          } else if (searchmom < 0) {
            this.searchesstatTitle = this.thisMonth
            //total searches in db this.searches.length
            this.searchesstatArrow = 'down'
            this.searchesstatPercent = searchmom
            this.searchesstatPercentColor = "text-red-500"
          }

          // New User stats header
          console.log(usermom)
          if (usermom >= 0) {
            this.userstatTitle = this.thisSevenDays.length
            //total searches in db this.searches.length
            this.userstatArrow = 'up'
            this.userstatPercent = usermom
            this.userstatPercentColor = "text-emerald-500"   
          } else if (usermom < 0) {
            this.userstatTitle = this.thisSevenDays.length
            //total searches in db this.searches.length
            this.userstatArrow = 'down'
            this.userstatPercent = usermom
            this.userstatPercentColor = "text-red-500"
          }

        })
        .catch(error => {
          console.log(error)
        })

      
      this.$store.commit('setIsLoading', false)
    }
  
  }
};
</script>
