<template>
<!-- ======= Resume Section ======= -->

    <section id="resume" class="resume">
      <div class="container">
        <div class="section-title">
          <h2>Resume</h2>
          <p> </p>
        </div>

        <div class="row" v-if="content">
          <div class="col-lg-6" data-aos="fade-up">            

            <h3 class="resume-title">Education</h3>

            <div class="resume-item" v-for="item in content.items[0].resume_education" :key="item">
              <h4>{{item.value.edu_title}}</h4>
              <h5>{{item.value.edu_start_date.toUpperCase()}} - {{item.value.edu_end_date.toUpperCase()}}</h5>
              <p v-html="item.value.edu_responsibilities"></p>
            </div>            

          </div>

          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">

            <h3 class="resume-title">Professional Experience</h3>

            <div class="resume-item" v-for="item in content.items[0].resume_experience" :key="item">
              <h4>{{item.value.job_title}}</h4>
              <h5>{{item.value.job_start_date.toUpperCase()}} - {{item.value.job_end_date.toUpperCase()}}</h5>
              <p v-html="item.value.job_responsibilities"></p>              
            </div>
            
          </div>
        </div>

      </div>
    </section><!-- End Resume Section -->
</template>

<script>
export default {
  name: 'Resume',
  props: {
    content: String,
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*--------------------------------------------------------------
# General
--------------------------------------------------------------*/
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
# Resume
--------------------------------------------------------------*/
.resume .resume-title {
  font-size: 26px;
  font-weight: 700;
  margin-top: 20px;
  margin-bottom: 20px;
  color: #050d18;
}

.resume .resume-item {
  padding: 0 0 20px 20px;
  margin-top: -2px;
  border-left: 2px solid #1f5297;
  position: relative;
}

.resume .resume-item h4 {
  line-height: 18px;
  font-size: 18px;
  font-weight: 600;
  text-transform: uppercase;
  font-family: "Poppins", sans-serif;
  color: #050d18;
  margin-bottom: 10px;
}

.resume .resume-item h5 {
  font-size: 16px;
  background: #e4edf9;
  padding: 5px 15px;
  display: inline-block;
  font-weight: 600;
  margin-bottom: 10px;
}

.resume .resume-item ul {
  padding-left: 20px;
}

.resume .resume-item ul li {
  padding-bottom: 10px;
}

.resume .resume-item:last-child {
  padding-bottom: 0;
}

.resume .resume-item::before {
  content: "";
  position: absolute;
  width: 16px;
  height: 16px;
  border-radius: 50px;
  left: -9px;
  top: 0;
  background: #fff;
  border: 2px solid #1f5297;
}
</style>
