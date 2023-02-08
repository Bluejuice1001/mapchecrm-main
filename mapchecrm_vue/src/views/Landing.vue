<template>
  <div>
    <navbar />
    <main>
      <div
        class="relative pt-16 pb-32 flex content-center items-center justify-center min-h-screen-75"
      >
        <div
          class="absolute top-0 w-full h-full bg-no-repeat bg-full bg-pink"
          :style="`background-image: url('${registerBg2}');`"
        >
        </div>
      </div>

      <section class="relative py-40">
        <div
          class="bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20"
          style="transform: translateZ(0);"
        >
          <svg
            class="absolute bottom-0 overflow-hidden"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="none"
            version="1.1"
            viewBox="0 0 2560 100"
            x="0"
            y="0"
          >
            <polygon
              class="text-white fill-current"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>

        <div class="container mx-auto px-4">
          <div class="items-center flex flex-wrap">
            <div class="w-full md:w-6/12 ml-auto mr-auto px-4">
              <div class="md:pr-10">
                <h1 class="text-5xl lg:text-6xl 2xl:text-7xl font-semibold">Add instant services to your website in one step</h1>
                <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
                  Press ( Ctrl+M | ⌘+M ) or the search icon to see us in action.
                </p>
                <ul class="list-none mt-6">
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-pink-600 bg-pink-200 mr-3"
                        >
                          <i class="fas fa-fingerprint"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Carefully crafted components
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-pink-600 bg-pink-200 mr-3"
                        >
                          <i class="fas fa-map-marker-alt"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Feasability
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-pink-600 bg-pink-200 mr-3"
                        >
                          <i class="far fa-paper-plane"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">Lead generation</h4>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
              <br/>
              <div class="flex items-center">
                <a class="widget-button bg-blueGray-800  text-white active:bg-blueGray-600 hover:bg-pink hover:text-white text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150 cursor-pointer" v-on:click="scrollMeTo('widget')">Get your free widget</a>
              </div>
            </div>
            <div class="w-full md:w-5/12 ml-auto mr-auto px-4">
              <img
                alt="..."
                class="max-w-full"
                src="../assets/img/overview.gif"
              />
            </div>
          </div>
        </div>
      </section>
      
      <section class="relative block pb-24 bg-lightBlue-400">
        <div
          class="bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20"
          style="transform: translateZ(0);"
        >
          <svg
            class="absolute bottom-0 overflow-hidden"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="none"
            version="1.1"
            viewBox="0 0 2560 100"
            x="0"
            y="0"
          >
            <polygon
              class="text-lightBlue-400 fill-current"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>
      </section>  
      
     <section ref="widget" class="flex flex-col gap-10 items-center justify-center min-h-screen relative md:pt-10 pb-20 max-w-full">
        <div class="container mx-auto px-4">
          <div class="flex flex-wrap justify-center text-center mb-12">
            <div class="w-full lg:w-6/12 px-4">
              <h2 class="text-4xl font-semibold">Create your own value chain</h2>
              <ul class="list-none mt-6 grid grid-cols-2 gap-1 justify-evenly">
              <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200 mr-3"
                        >
                          <i class="fas fa-fingerprint"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Customize your services
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200 mr-3"
                        >
                          <i class="fas fa-fingerprint"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Intergate 3rd party API
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200 mr-3"
                        >
                          <i class="far fa-paper-plane"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Expand your footprint
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200 mr-3"
                        >
                          <i class="far fa-paper-plane"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Extend your widget to resellers</h4>
                      </div>
                    </div>
                  </li>
                </ul>
                <br/>
                <div class="flex items-center justify-center px-4">
              <a class="widget-button bg-blueGray-800  text-white active:bg-blueGray-600 hover:bg-mapchiblue hover:text-white text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150 cursor-pointer" v-on:click="scrollMeTo('contact')">Custom Requirments</a>
              </div>
            </div>
          </div>

          <div class="container mx-auto max-w-xl px-4 lg:pt-20 lg:pb-48 ">
            <div class="text-2xl sm:text-2xl flex gap-2 px-4">
              <h3 class="font-semibold whitespace-nowrap">Step 1 -</h3>
              <h3>Add this to your website {{ code }}</h3>
            </div>
<!--Clipboard & Code Section-->
<div class="pt-4 max-w-full gap-2 relative">
<div class="text-base mx-auto rounded-none sm:rounded w-full max-w-xl border border-gray-300 bg-gray-800 overflow-x-auto" data-type="html">
 <button class="text-white font-semibold absolute top-4 right-1  hover:text-mapchi" v-on:click="CopyToClipboard('sample')" id="copybtn">Copy</button>
<pre id="copy" class="bg-gray-800 pt-8">   <span class="text-gray-500">&lt;</span><span class="text-mapchi">script</span> <span class="text-mapchiblue">mapchi-key</span><span class="text-gray-500">=</span><span class="text-orange-500">{{this.uuidv4}}</span> <span class="text-mapchiblue">type</span><span class="text-gray-500">=</span><span class="text-orange-500">"module"</span> <span class="text-gray-200">crossorigin</span> <span class="text-mapchiblue">src</span><span class="text-gray-500">=</span><span class="text-orange-500">"https://cdn.jsdelivr.net/gh/MapcheSearch/mapche-search-widget@0.1.1/dist/index.js"</span><span class="text-gray-500">&gt;</span><span class="text-gray-500">&lt;/</span><span class="text-mapchi">script</span><span class="text-gray-500">&gt;</span>
   <span class="text-green-500">&lt;!--next line is optional to preload modules--&gt;</span>
   <span class="text-gray-500">&lt;</span><span class="text-mapchi">link</span> <span class="text-mapchiblue">rel</span><span class="text-gray-500">=</span><span class="text-orange-500">"modulepreload"</span> <span class="text-mapchiblue">href</span><span class="text-gray-500">=</span><span class="text-orange-500">"https://cdn.jsdelivr.net/gh/MapcheSearch/mapche-search-widget@0.1.1/dist/vendor2.js"</span><span class="text-gray-500">&gt;</span>

</pre>
</div>
</div>
</div>
      <div class="container mx-auto max-w-xl px-4 pt-12 lg:pb-48 ">
            <div class="text-2xl sm:text-2xl flex gap-2 px-4">
              <h3 class="font-semibold whitespace-nowrap">Step 2 -</h3>
              <h3>Create account (optional)</h3>
            </div>
            <ul class="list-none mt-6 grid grid-cols-2 gap-1 justify-evenly">
              <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200 mr-3"
                        >
                          <i class="fas fa-fingerprint"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Admin Dashboard
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200 mr-3"
                        >
                          <i class="fas fa-fingerprint"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Feasability Engine
                        </h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200 mr-3"
                        >
                          <i class="far fa-paper-plane"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Search Results</h4>
                      </div>
                    </div>
                  </li>
                  <li class="py-2">
                    <div class="flex items-center">
                      <div>
                        <span
                          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-lightBlue-600 bg-lightBlue-200 mr-3"
                        >
                          <i class="far fa-paper-plane"></i>
                        </span>
                      </div>
                      <div>
                        <h4 class="text-blueGray-500">
                          Leads Generated</h4>
                      </div>
                    </div>
                  </li>
                </ul>
                <br/>
                <div class="flex items-center justify-center px-4">
                <router-link to="/auth/register"
                class="bg-blueGray-800  text-white active:bg-blueGray-600 hover:bg-mapchiblue hover:text-white text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150">
                  Register
                </router-link>
              </div>  
          </div>
        </div>
      </section>

      <section ref="contact" class="pb-20 relative block bg-blueGray-800">
        <div
          class="bottom-auto top-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden -mt-20 h-20"
          style="transform: translateZ(0);"
        >
          <svg
            class="absolute bottom-0 overflow-hidden"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="none"
            version="1.1"
            viewBox="0 0 2560 100"
            x="0"
            y="0"
          >
            <polygon
              class="text-blueGray-800 fill-current"
              points="2560 0 2560 100 0 100"
            ></polygon>
          </svg>
        </div>

        <div class="container mx-auto px-4 lg:pt-24 lg:pb-64">
          <div class="flex flex-wrap text-center justify-center">
            <div class="w-full lg:w-6/12 px-4">
              <h2 class="text-4xl font-semibold text-white pt-8">
                Grow your business
              </h2>
              <p class="text-lg leading-relaxed mt-4 mb-4 text-blueGray-400">
                Expand your business presenance, with a click of a button you can start selling new services. Let macphi do the selling for you
              </p>
            </div>
          </div>
          <div class="flex flex-wrap mt-12 justify-center">
            <div class="w-full lg:w-3/12 px-4 text-center">
              <div
                class="text-blueGray-800 p-3 w-12 h-12 shadow-lg rounded-full bg-white inline-flex items-center justify-center"
              >
                <i class="fas fa-medal text-xl"></i>
              </div>
              <h6 class="text-xl mt-5 font-semibold text-white">
                Excelent Services
              </h6>
              <p class="mt-2 mb-4 text-blueGray-400">
                Connectivity, Voice, Cloud, Cellular. Sell any service you can think of to expand your market growth.
              </p>
            </div>
            <div class="w-full lg:w-3/12 px-4 text-center">
              <div
                class="text-blueGray-800 p-3 w-12 h-12 shadow-lg rounded-full bg-white inline-flex items-center justify-center"
              >
                <i class="fas fa-poll text-xl"></i>
              </div>
              <h5 class="text-xl mt-5 font-semibold text-white">
                Grow your market
              </h5>
              <p class="mt-2 mb-4 text-blueGray-400">
                Extending your footprint to all your potentail clients and resellers become a easy task.
              </p>
            </div>
            <div class="w-full lg:w-3/12 px-4 text-center">
              <div
                class="text-blueGray-800 p-3 w-12 h-12 shadow-lg rounded-full bg-white inline-flex items-center justify-center"
              >
                <i class="fas fa-lightbulb text-xl"></i>
              </div>
              <h5 class="text-xl mt-5 font-semibold text-white">
                Launch time
              </h5>
              <p class="mt-2 mb-4 text-blueGray-400">
                With 2 lines of code, you and launch your new business in seconds.
              </p>
              <br/>
            </div>
          </div>
        </div>
      </section>
      <section class="relative block py-24 lg:pt-0 bg-blueGray-800">
        <div class="container mx-auto px-4">
          <div class="flex flex-wrap justify-center lg:-mt-64 -mt-48">
            <div class="w-full lg:w-6/12 px-4">
              <div
                class="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200"
              >
                <div class="flex-auto p-5 lg:p-10">
                  <h4 class="text-2xl font-semibold">
                    Want to work with us?
                  </h4>
                  <p class="leading-relaxed mt-1 mb-4 text-blueGray-500">
                    Complete the form below and we will get back to you, soonest.
                  </p>
                  <div class="relative w-full mb-3 mt-8">
                    <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="full-name"
                    >
                      Full Name
                    </label>
                    <input
                      type="text"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Full Name"
                    />
                  </div>

                  <div class="relative w-full mb-3">
                    <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="email"
                    >
                      Email
                    </label>
                    <input
                      type="email"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Email"
                    />
                  </div>

                  <div class="relative w-full mb-3">
                    <label
                      class="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                      htmlFor="message"
                    >
                      Message
                    </label>
                    <textarea
                      rows="4"
                      cols="80"
                      class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full"
                      placeholder="Type a message..."
                    />
                  </div>
                  <div class="text-center mt-6">
                    <button
                      class="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                      type="button"
                    >
                      Send Message
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <footer-component />
  </div>
</template>
<script>
import Navbar from "@/components/Navbars/AuthNavbar.vue";
import FooterComponent from "@/components/Footers/Footer.vue";
import registerBg2 from "@/assets/img/register_bg_2.png";

export default {
  async mounted () {
    this.uuidv4 = await uuidv4get()
    function uuidv4get() {
        return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
          (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
        );        
      }
  },

  data() {
    return {
      uuidv4: '00000000-0000-0000-0000-000000000000',
      registerBg2,
      code: `<head>`
    };
  },

  components: {
    Navbar,
    FooterComponent,
  },

  methods: {
  scrollMeTo(refName) {
    var element = this.$refs[refName];
    var top = element.offsetTop;

    window.scrollTo(0, top);
  },
  CopyToClipboard() {
          const copyText = document.getElementById("copy").
          textContent
          const btn = document.getElementById("copybtn")
          const textArea = document.createElement('textarea')
          textArea.textContent = copyText
          document.body.append(textArea)
          textArea.select()
          document.execCommand("copy")
          const intialText = "Copy"
          if (btn.textContent.includes(intialText)) {
            btn.textContent = "Copied!"
          } else {
            btn.textContent = intialText
          }
      }
}

};
</script>
<style strict>

textarea {
  position: absolute;
  left: -9999px
}
</style>
