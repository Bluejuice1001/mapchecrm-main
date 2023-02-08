<template>
  <nav
    class="top-0 absolute z-50 w-full flex flex-wrap items-center justify-between px-2 py-3 navbar-expand-lg"
  >
    <div
      class="container px-4 mx-auto flex flex-wrap items-center justify-between"
    >
      <div
        class="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start"
      >
        <router-link
          class="text-white text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase"
          to="/"
        >
        
        <img src="https://res.cloudinary.com/vidmax/image/upload/v1673423184/mapchi-websitelogo2_u7fr9a.png" class="h-24">
        </router-link>
        <button
          class="h-10 cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
          type="button"
          v-on:click="setNavbarOpen"
        >
          <i class="text-white fas fa-bars"></i>
        </button>
      </div>
     <div
        class="lg:flex flex-grow items-center bg-white lg:bg-opacity-0 lg:shadow-none"
        :class="[navbarOpen ? 'block rounded shadow-lg' : 'hidden']"
        id="example-navbar-warning"
      >
        <ul class="flex flex-col lg:flex-row list-none lg:ml-auto">
          <li class="flex items-center">
          <!--  <PagesDropdown />-->
            <router-link
              to="/auth/login"
              class="lg:text-white lg:hover:text-blueGray-700 hover:text-blueGray-500 text-blueGray-700 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold"
            >
              Login
            </router-link>
          </li>
          <li class="flex items-center">
            <router-link
              to="/auth/register"
              class="lg:text-white lg:hover:text-blueGray-700 hover:text-blueGray-500 text-blueGray-700 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold"
            >
              Register
            </router-link>
          </li>

          <li class="flex items-center">
            <a
              class="lg:text-white lg:hover:text-blueGray-700 text-blueGray-700 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold"
              href="https://www.facebook.com/sharer/sharer.php?u=https://mapchi.com"
              target="_blank"
            >
              <i
                class="lg:text-blueGray-200 lg:hover:text-blueGray-700 hover:text-blueGray-500 text-blueGray-400 fab fa-facebook text-lg leading-lg"
              />
              <span class="lg:hidden inline-block ml-2 hover:text-blueGray-500">Share</span>
            </a>
          </li>

          <li class="flex items-center">
            <a
              class="lg:text-white lg:hover:text-blueGray-700  text-blueGray-700 px-3 py-4 lg:py-2 flex items-center text-xs uppercase font-bold"
              href="https://twitter.com/intent/tweet?url=https://mapchi.com&text=Add%20instant%20services%20to%20a%20your%20website%20in%20one%20step.%20Grow%20your%20business%20with%20mapchi"
              target="_blank"
            >
              <i
                class="lg:text-blueGray-200 lg:hover:text-blueGray-700 hover:text-blueGray-500 text-blueGray-400 fab fa-twitter text-lg leading-lg"
              />
              <span class="lg:hidden inline-block ml-2 hover:text-blueGray-500">Tweet</span>
            </a>
          </li>


        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
//import PagesDropdown from "@/components/Dropdowns/PagesDropdown.vue";
export default {
  data() {
    return {
      navbarOpen: false,
    };
  },
  methods: {
    setNavbarOpen: function () {
      this.navbarOpen = !this.navbarOpen;
    },
  },
  components: {
//    PagesDropdown,
  },
};
</script>
