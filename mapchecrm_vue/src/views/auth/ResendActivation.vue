<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-4/12 px-4">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0"
        >
          <div class="rounded-t mb-0 px-6 py-5">
            <div class="text-center mb-3">
              <h6 class="text-blueGray-500 text-sm font-bold">
                Resend Activation Link
              </h6>
            </div>

          </div>
          <div class="flex-auto px-4 lg:px-10 py-10 pt-0">
            <form @submit.prevent="submitForm">
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Email
                </label>
                <input
                  type="email"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Email"
                  v-model="username"
                />
              </div>

              <div class="notification is-primary" v-if="errors.length">
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>
              <div class="text-center mt-6">
                <button
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                >
                  Submit
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import { toast } from 'bulma-toast'

export default {
  name: 'ResendActivation',
  data() {
    return {
      username: '',
      errors: []
    };
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('The email is missing')
      }

      if (!this.errors.length) {  
      this.$store.commit('setIsLoading', true)

        const formData = {
          email: this.username
        }

        
      await axios
          .post('/accounts/users/resend_activation/', formData)
          .then(response => {
                toast({
                  message: 'If the account is not active, an email will be sent with instructions!',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 5000,
                  position: 'bottom-right',
                })
                this.$router.push('/')
            }) 
            .catch(error => {
             if(error.response) {
                for (const property in error.response.data) {
                  this.email = ''
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else if (error.message) {
                  this.email = ''
                  this.errors.push('Something went wrong. Please try again!')
              }
            })

          this.$store.commit('setIsLoading', false)
      }
    }
  }
}
</script>