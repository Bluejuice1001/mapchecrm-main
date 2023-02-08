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
                Sign in
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
                  class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                  placeholder="Password"
                  v-model="password"
                />
              </div>
             <br/>
              <div class="notification is-primary" v-if="errors.length">
                  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
              </div>
              <div class="text-center mt-6">
                <button
                  class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                >
                  Sign In
                </button>
              </div>
            </form>
          </div>
        </div>
        <div class="flex flex-wrap mt-6 relative">
          <div class="w-1/2">
            <router-link to="/auth/password_reset" class="text-blueGray-200">
              <small>Forgot password?</small>
            </router-link>
          </div>
          <div class="w-1/2 text-right">
            <router-link to="/auth/register" class="text-blueGray-200">
              <small>Create new account</small>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';


export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    };
  },
  methods: {
    async submitForm() {
        this.$store.commit('setIsLoading', true)
        this.errors = []
        axios.defaults.headers.common['Authorization'] = ''
        localStorage.removeItem('token')
        localStorage.removeItem('key')

        const formData = {
          username: this.username,
          password: this.password
        }

        await axios
          .post('/accounts/token/login/', formData)
          .then(response => {
            const token = response.data.auth_token

            this.$store.commit('setToken', token)  //commit calls mutations funtions in index.js store to initialize authentication token
            
            axios.defaults.headers.common['Authorization'] = 'Token ' + token

            localStorage.setItem('token', token)

            this.$router.push('/admin/my-account')
          })
          .catch(error => {
              if(error.response) {
                for (const property in error.response.data) {
                  this.password = ''
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
              } else if (error.message) {
                  this.password = ''
                  this.errors.push('Something went wrong. Please try again!')
              }
            })
        
          this.$store.commit('setIsLoading', false)
    }
  }
};
</script>
