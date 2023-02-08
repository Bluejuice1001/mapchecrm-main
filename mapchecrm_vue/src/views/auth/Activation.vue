<template>
          <div class="notification is-danger" v-if="errors.length">
             <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
</template>
<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'Activation',
  data() {
    return {
      errors: []
    };
  },

  mounted(){
    this.$nextTick(this.submitForm)
  },
  methods: {
    async submitForm() {

      this.errors = []

      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)

        const uid = this.$route.params.uid
        const token = this.$route.params.token

        const formData = {
          uid: uid,
          token: token
        }
        
        //Log if uid, token exists, remove when go live
        //console.log(formData)  
       
        await axios
            .post('/accounts/users/activation/', formData)
            .then(response => {
                toast({
                  message: 'Account successfuly activated, you can proceed to login',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 5000,
                  position: 'bottom-right',
                })
                this.$router.push('/auth/login')
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
    },

  }
}
</script>