<template>
  <div class="container mx-auto px-4 h-full">
    <div class="flex content-center items-center justify-center h-full">
      <div class="w-full lg:w-6/12 px-4">
        <div
          class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0"
        >
          <div class="rounded-t mb-0 px-6 py-5">
            <div class="text-center mb-3">
              <h6 class="text-blueGray-500 text-sm font-bold">
                Sign up
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

              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Password
                </label>
                <input
                  type="password"
                  name="password1"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Password"
                  v-model="password1"
                />
              </div>
              <div class="relative w-full mb-3">
                <label
                  class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                  htmlFor="grid-password"
                >
                  Repeat Password
                </label>
                <input
                  type="password"
                  name="password2"
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Password"
                  v-model="password2"
                />
              </div>

              <div>
                <label class="inline-flex items-center cursor-pointer">
                  <input
                    id="customCheckLogin"
                    type="checkbox"
                    v-model="checked"
                    class="form-checkbox border-0 rounded text-blueGray-700 ml-1 w-5 h-5 ease-linear transition-all duration-150"
                  />
                  <span class="ml-2 text-sm font-semibold text-blueGray-600">
                    I agree with the
                    <a href="javascript:void(0)" class="text-emerald-privacy">
                      Privacy Policy
                    </a>
                  </span>
                </label>
              </div>
              <br/>
              <div class="notification is-primary" v-if="errors.length">
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>
              <div v-if="checked" class="text-center mt-6">
                <button
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                >
                  Create Account
                </button>
              </div>
            </form>
          </div>
        </div>
        <div class="flex flex-wrap mt-6 relative">
          <div class="w-1/2">
            <router-link to="/auth/resend_activation" class="text-blueGray-200">
              <small>Resend Activation Link?</small>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

import {toast} from 'bulma-toast'


export default {
  name: 'Register',
  data() {
    return {
      username: '',
      password1: '',
      password2: '',
      checked: false,
      errors: []
    };
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('The username is missing')
      }

      if (this.password1 === '') {
        this.errors.push('The password is too short')
        this.password1 = ''
        this.password2 = ''
        this.checked = false
      }

      if (this.password1 !== this.password2) {
        this.errors.push('The passwords are not matching')
        this.password1 = ''
        this.password2 = ''
        this.checked = false
      }


      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)

        const formData = {
          username: this.username,
          email: this.username,
          password: this.password1
        }

        await axios
            .post('/accounts/users/', formData)
            .then(response => {
                toast({
                  message: 'Please activate your account, an email with instructions has been send',
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
                  this.password1 = ''
                  this.password2 = ''
                  this.username = ''
                  this.checked = false
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else if (error.message) {
                  this.password1 = ''
                  this.password2 = ''
                  this.username = ''
                  this.checked = false
                  this.errors.push('Something went wrong. Please try again!')
              }
            })

          this.$store.commit('setIsLoading', false)
      }
    }
  }
};
</script>
