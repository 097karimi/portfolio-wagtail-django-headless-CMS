<template>
        <div id='about' class="container col-xxl-12 px-4 py-5" v-if="content">
            <div class="row flex-lg-row-reverse align-items-center g-5 py-5">
            <div class="col-10 col-sm-8 col-lg-6">
                <img v-if="content.items[0].my_image" :src=" 'http://127.0.0.1:8000' + content.items[0].my_image.meta.download_url" class="d-block mx-lg-auto img-fluid" alt="The Image hasn't been loaded!" width="700" height="500" loading="lazy">
            </div>
            <div class="col-lg-6">
                <h1 class="display-5 fw-bold lh-1 mb-3" v-html="content.items[0].about_me_title"></h1>
                <p class="lead" v-html="content.items[0].about_me"></p>
                <div class="d-grid gap-2 d-md-flex justify-content-md-start">
                <a href="#resume" class="btn btn-primary btn-lg px-4 me-md-2">Know me more!</a>
                <a href="#contact" class="btn btn-outline-secondary btn-lg px-4">Contact Me</a>
                </div>
            </div>
            </div>
        </div>
</template>

<script>
export default {
  name: 'Cover',  
  props: {
    content: String,
  },
  data() {
      return {
          picture : '../src/assets/bootstrap-docs.png',
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.b-example-divider {
  height: 3rem;
  background-color: rgba(0, 0, 0, .1);
  border: solid rgba(0, 0, 0, .15);
  border-width: 1px 0;
  box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
}

@media (min-width: 992px) {
  .rounded-lg-3 { border-radius: .3rem; }
}

img {
  border-radius: 50%;
}
</style>
