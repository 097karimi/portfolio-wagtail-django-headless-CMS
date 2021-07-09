<template>
<!-- ======= Skills Section ======= -->
    <section id="skills" class="skills section-bg">
      <div class="container">

        <div class="section-title">
          <h2>Skills</h2>
          <p v-if="content" v-html="content.items[0].skill_discription"></p>
        </div>

        <div class="row skills-content" v-if="content">

          <div class="col-lg-6" data-aos="fade-up" v-for="item in content.items[0].skills" :key="item">

            <div class="progress" >
              <span class="skill"  >{{ item.value.skill_title }}<i class="val">{{ item.value.skill_level }}%</i></span>
              <div class="progress-bar-wrap">
                <div class="progress-bar" role="progressbar" :aria-valuenow="item.value.skill_level" aria-valuemin="0" aria-valuemax="100" :style="{ width: item.value.skill_level + '%' }" ></div>
              </div>
            </div>

          </div>

        </div>

      </div>
    </section><!-- End Skills Section -->
</template>


<script>

export default {
  name: 'HelloWorld',
  props: {
    content: String,
  },
  mounted() {
  },
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
# Skills
--------------------------------------------------------------*/

.skills .progress {
  height: 60px;
  display: block;
  background: none;
  border-radius: 0;
}

.skills .progress .skill {
  padding: 0;
  margin: 0 0 6px 0;
  text-transform: uppercase;
  display: block;
  font-weight: 600;
  font-family: "Poppins", sans-serif;
  color: #050d18;
}

.skills .progress .skill .val {
  float: right;
  font-style: normal;
}

.skills .progress-bar-wrap {
  background: #dce8f8;
  height: 10px;
}

.skills .progress-bar {
  width: 1px;
  height: 10px;
  transition: .9s;
  background-color: #149ddd;
}
</style>
