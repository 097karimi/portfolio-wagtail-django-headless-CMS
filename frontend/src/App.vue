<template>

  <!-- Navbar -->
  <Navbar/>

  <!-- Cover -->
  <Cover :content="info" />

  <!-- Resume -->
  <Resume :content="info" />

  <!-- Skills -->
  <Skills :content="info" />

  <!-- Projects -->
  <Projects :content="info" />

  <!-- Area Of Interests -->
  <AreasOfInterest :content="info" />

  <!-- Contact -->
  <Contact :content="info" />

  <!-- Footer -->
  <Footer :content="info" />
  
  <!-- BackToTop -->
  <BackToTop/>
  
    
</template>

<script>

import Navbar from './components/Navbar'
import Cover from './components/Cover'
import Contact from './components/Contact'
import Footer from './components/Footer'
import Skills from './components/Skills'
import Resume from './components/Resume'
import Projects from './components/Projects'
import AreasOfInterest from './components/AreasOfInterest'
import BackToTop from './components/BackToTop'
import axios from 'axios'


export default {
  name: 'App',
  components: {
    Navbar,
    Cover,
    Resume,
    Contact,
    Footer,
    Skills,
    Projects,
    AreasOfInterest,
    BackToTop,
  },
  data () {
    return {
      info: null,
      //host: location.host,
      loading: true,
      errored: false
    }
  },
  mounted () {
    axios  //this.host +
      .get('http://127.0.0.1:8000/api/v2/pages/?type=home.HomePage&fields=about_me_title,about_me,my_image,resume_experience,resume_education,skill_discription,skills,recent_projects,areas_of_interest,linkedin,github,telegram,my_services,address,call_me,email_me,open_hours,about_me_footer')
      .then(response => (this.info = response.data))  

      .catch(error => {
          console.log(error)
          this.errored = true
        })

      .finally(() => this.loading = false)  
  }
}
</script>

<style>

</style>
