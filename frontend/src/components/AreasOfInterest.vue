<template>
<!-- ======= Area of interest Section ======= -->
    <section id="areas_of_interest" class="services" >
      <div class="container">

        <div class="section-title">
          <h2>Areas Of interest</h2>
          <p></p>
        </div>

        <div class="row" v-if="content">

          <div v-for="item in content.items[0].areas_of_interest" :key="item" class="col-lg-4 col-md-6 icon-box" data-aos="fade-up" data-aos-delay="300">
            <div class="icon"><i class="bi bi-code-slash"></i></div>
            <h4 class="title"><a href="">{{item.value.areas_of_interest_title}}</a></h4>
            <p class="description" v-html="item.value.areas_of_interest_discription"></p>
          </div>

        </div>

      </div>
    </section><!-- End Services Section -->
</template>

<script>
export default {
  name: 'AreasOfInterest',
  props: {
    content: String,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  font-family: "Open Sans", sans-serif;
  color: #272829;
}

a {
  color: #149ddd;
  text-decoration: none;
}

a:hover {
  color: #37b3ed;
  text-decoration: none;
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Raleway", sans-serif;
}

/*--------------------------------------------------------------
# Sections General
--------------------------------------------------------------*/
section {
  padding: 60px 0;
  overflow: hidden;
}

.section-bg {
  background: #f5f8fd;
}

.section-title {
  padding-bottom: 30px;
}

.section-title h2 {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 20px;
  padding-bottom: 20px;
  position: relative;
  color: #173b6c;
}

.section-title h2::after {
  content: '';
  position: absolute;
  display: block;
  width: 50px;
  height: 3px;
  background: #149ddd;
  bottom: 0;
  left: 0;
}

.section-title p {
  margin-bottom: 0;
}

/*--------------------------------------------------------------
# Services
--------------------------------------------------------------*/
.services .icon-box {
  margin-bottom: 20px;
}

.services .icon {
  float: left;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 54px;
  height: 54px;
  background: #149ddd;
  border-radius: 50%;
  transition: 0.5s;
  border: 1px solid #149ddd;
}

.services .icon i {
  color: #fff;
  font-size: 24px;
  line-height: 0;
}

.services .icon-box:hover .icon {
  background: #fff;
}

.services .icon-box:hover .icon i {
  color: #149ddd;
}

.services .title {
  margin-left: 80px;
  font-weight: 700;
  margin-bottom: 15px;
  font-size: 18px;
}

.services .title a {
  color: #343a40;
}

.services .title a:hover {
  color: #149ddd;
}

.services .description {
  margin-left: 80px;
  line-height: 24px;
  font-size: 14px;
}
</style>
