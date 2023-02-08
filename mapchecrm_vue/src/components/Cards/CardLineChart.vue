<template>
  <div
    class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded bg-blueGray-700"
  >
    <div class="rounded-t mb-0 px-4 py-3 bg-transparent">
      <div class="flex flex-wrap items-center">
        <div class="relative w-full max-w-full flex-grow flex-1">
          <h6 class="uppercase text-blueGray-100 mb-1 text-xs font-semibold">
            Overview
          </h6>
          <h2 class="text-white text-xl font-semibold">
            Searches
          </h2>
        </div>
      </div>
    </div>
    <div class="p-4 flex-auto">
      <!-- Chart -->
      <div class="relative h-350-px">
        <canvas id="line-chart"></canvas>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import Chart from "chart.js"
import moment from 'moment'
import _ from 'lodash'
import { throwStatement } from '@babel/types';

export default {
  mounted: function () {
    this.getSearches()
  },
  
  data() {
    return {
      index: 0,
      currIndex: 0,
      searches: [],
      currData: [],
      prevData: []
    }
  },

  methods: {

    getMonthDifference(startDate, endDate) {
      return (
        endDate.getMonth() -
        startDate.getMonth() +
        12 * (endDate.getFullYear() - startDate.getFullYear())
      );
    },

    async getSearches() {
      this.$store.commit('setIsLoading', true)

      axios
        .get('/mapche-api/v1/search/')
        .then(response => {
          this.searches = response.data
       
          let currYear = moment().year()  
          let prevYear = moment().year() - 1

          for (var x = 0; x < 12; x++) {

            for (var i = 0; i < response.data.length; i++) {
            
              let searchData = response.data[i].created_at
              let dateString = new Date(searchData).getMonth() //return 1 - 12
    
              //returns full year 2021, 2022, 2023 etc.
              let dateYear = new Date(searchData).getFullYear()

              if (dateYear === currYear) { 
                if (dateString === x) {
                  this.currIndex = this.currIndex + 1
                }
              } else if (dateYear === prevYear) {
                if (dateString === x) {
                  this.index = this.index + 1
                }
              }
            }

            this.currData.push({'currMonth': this.currIndex})
            this.currIndex = 0
            this.prevData.push({'prevMonth': this.index})
            this.index = 0
          }

          var config = {
            type: "line",
              data: {
                labels: [
                  "January",
                  "February",
                  "March",
                  "April",
                  "May",
                  "June",
                  "July",
                  "August",
                  "September",
                  "October",
                  "November",
                  "December"
                ],
                datasets: [
                        {
                          label: new Date().getFullYear(), //currYear
                          backgroundColor: "#4c51bf",
                          borderColor: "#4c51bf",
                          data: [this.currData[0].currMonth,this.currData[1].currMonth,this.currData[2].currMonth,this.currData[3].currMonth,this.currData[4].currMonth,this.currData[5].currMonth,this.currData[6].currMonth,this.currData[7].currMonth,this.currData[8].currMonth,this.currData[9].currMonth,this.currData[10].currMonth,this.currData[11].currMonth],
                          fill: false,
                        },
                        {
                          label: new Date().getFullYear() - 1, //prevYear
                          fill: false,
                          backgroundColor: "#fff",
                          borderColor: "#fff",
                          data: [this.prevData[0].prevMonth,this.prevData[1].prevMonth,this.prevData[2].prevMonth,this.prevData[3].prevMonth,this.prevData[4].prevMonth,this.prevData[5].prevMonth,this.prevData[6].prevMonth,this.prevData[7].prevMonth,this.prevData[8].prevMonth,this.prevData[9].prevMonth,this.prevData[10].prevMonth,this.prevData[11].prevMonth],
                        },
                ],
              },
              options: {
                maintainAspectRatio: false,
                responsive: true,
                title: {
                  display: false,
                  text: "Searches Charts",
                  fontColor: "white",
                },
                legend: {
                  labels: {
                    fontColor: "white",
                  },
                  align: "end",
                  position: "bottom",
                },
                tooltips: {
                  mode: "index",
                  intersect: false,
                },
                hover: {
                  mode: "nearest",
                  intersect: true,
                },
                scales: {
                  xAxes: [
                    {
                      ticks: {
                        fontColor: "rgba(255,255,255,.7)",
                      },
                      display: true,
                      scaleLabel: {
                        display: false,
                        labelString: "Month",
                        fontColor: "white",
                      },
                      gridLines: {
                        display: false,
                        borderDash: [2],
                        borderDashOffset: [2],
                        color: "rgba(33, 37, 41, 0.3)",
                        zeroLineColor: "rgba(0, 0, 0, 0)",
                        zeroLineBorderDash: [2],
                        zeroLineBorderDashOffset: [2],
                      },
                    },
                  ],
                  yAxes: [
                    {
                      ticks: {
                        fontColor: "rgba(255,255,255,.7)",
                      },
                      display: true,
                      scaleLabel: {
                        display: false,
                        labelString: "Value",
                        fontColor: "white",
                      },
                      gridLines: {
                        borderDash: [3],
                        borderDashOffset: [3],
                        drawBorder: false,
                        color: "rgba(255, 255, 255, 0.15)",
                        zeroLineColor: "rgba(33, 37, 41, 0)",
                        zeroLineBorderDash: [2],
                        zeroLineBorderDashOffset: [2],
                      },
                    },
                  ],
                },
              },
          };

          var ctx = document.getElementById("line-chart").getContext("2d")
          window.myLine = new Chart(ctx, config)

        })
        .catch(error => {
          console.log(error)
        })

      
      this.$store.commit('setIsLoading', false)
    }
  
  }

};
</script>
