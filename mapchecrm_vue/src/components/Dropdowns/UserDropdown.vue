<template>
  <div>
    <a
      class="text-blueGray-500 block"
      href="#pablo"
      ref="btnDropdownRef"
      v-on:click="toggleDropdown($event)"
    >
      <div class="items-center flex">
        <span
          class="w-12 h-12 text-sm text-white bg-blueGray-200 inline-flex items-center justify-center rounded-full"
        >
          <img
            alt="..."
            class="w-full rounded-full align-middle border-none shadow-lg"
            :src="image"
          />
        </span>
      </div>
    </a>
    <div
      ref="popoverDropdownRef"
      class="bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48"
      v-bind:class="{
        hidden: !dropdownPopoverShow,
        block: dropdownPopoverShow,
      }"
    >

      <a
        href="javascript:void(0);"
        class="text-xs uppercase py-2 px-4 block w-full whitespace-nowrap bg-transparent hover:text-blueGray-500 text-blueGray-700 font-bold"
      >
        My Account
      </a>
      <a
        href="javascript:void(0);"
        class="text-xs uppercase py-2 px-4 block w-full whitespace-nowrap bg-transparent hover:text-blueGray-500 text-blueGray-700 font-bold"
      >
        Settings
      </a>

      <div class="h-0 my-2 border border-solid border-blueGray-100" />
      <button 
      v-on:click="logout()"
      class="text-xs text-left uppercase py-2 px-4 block w-full whitespace-nowrap bg-transparent hover:text-blueGray-500 text-blueGray-700 font-bold"
      >
        Logout
      </button>
    </div>
  </div>
</template>

<script>
import { createPopper } from "@popperjs/core";
import image from "@/assets/img/team-1-800x800.jpg";
import axios from 'axios'

export default {
  data() {
    return {
      dropdownPopoverShow: false,
      image: image,
    };
  },
  methods: {
    toggleDropdown: function (event) {
      event.preventDefault();
      if (this.dropdownPopoverShow) {
        this.dropdownPopoverShow = false;
      } else {
        this.dropdownPopoverShow = true;
        createPopper(this.$refs.btnDropdownRef, this.$refs.popoverDropdownRef, {
          placement: "bottom-start",
        });
      }
    },
    async logout() {
      await axios
          .post('/accounts/token/logout')
          .then(response => {
            console.log('Logged out')
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })

      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('token')
      this.$store.commit('removeToken')    
      this.$router.push('/')
    }
  },
};
</script>
