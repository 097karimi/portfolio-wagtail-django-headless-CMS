<template>
    <!-- ======= Recent Projects Section ======= -->
    <section id="projects" class="recent-blog-posts">

      <div class="container" data-aos="fade-up">

        <header class="section-title">
          <h2>Projects</h2>
          <p>Recent Projects</p>
        </header>
        

        <div class="row" v-if="content">

            <div class="col-lg-4" v-for="item in content.items[0].recent_projects" :key="item">
              <div class="post-box">
                <div class="post-img" v-for="item_img in image_url.items" :key="item_img">
                  <img  v-if="item_img.id == item.value.project_image" :src="'http://127.0.0.1:8000' + item_img.meta.download_url" class="img-fluid" alt="">
                </div>
                <span class="post-date" v-if="content" v-html="item.value.project_date"></span>
                <h3 class="post-title" v-if="content" v-html="item.value.project_title"></h3>
                <a :href=item.value.project_github_url class="readmore stretched-link mt-auto" v-if="content"><span>Github</span><i class="bi bi-arrow-right"></i></a>
              </div>
            </div>  

        </div>

      </div>

    </section><!-- End Recent Blog Posts Section -->
</template>


<script>
import axios from 'axios'

export default {
  name: 'Projects',
  props:{
    content: String,
  },
  data () {
    return{
      image_url: null,
      host: location.host
    }      
  },
  mounted () {
    axios  //this.host +
      .get('http://127.0.0.1:8000/api/v2/images/')
      .then(response => (this.image_url = response.data))  
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
# Recent Blog Posts
--------------------------------------------------------------*/
.recent-blog-posts .post-box {
  box-shadow: 0px 0 30px rgba(1, 41, 112, 0.08);
  transition: 0.3s;
  height: 100%;
  overflow: hidden;
  padding: 30px;
  border-radius: 8px;
  position: relative;
  display: flex;
  flex-direction: column;
}

.recent-blog-posts .post-box .post-img {
  overflow: hidden;
  margin: -30px -30px 15px -30px;
  position: relative;
}

.recent-blog-posts .post-box .post-img img {
  transition: 0.5s;
}

.recent-blog-posts .post-box .post-date {
  font-size: 16px;
  font-weight: 600;
  color: rgba(1, 41, 112, 0.6);
  display: block;
  margin-bottom: 10px;
}

.recent-blog-posts .post-box .post-title {
  font-size: 24px;
  color: #012970;
  font-weight: 700;
  margin-bottom: 18px;
  position: relative;
  transition: 0.3s;
}

.recent-blog-posts .post-box .readmore {
  display: flex;
  align-items: center;
  font-weight: 600;
  line-height: 1;
  transition: 0.3s;
}

.recent-blog-posts .post-box .readmore i {
  line-height: 0;
  margin-left: 4px;
  font-size: 18px;
}

.recent-blog-posts .post-box:hover .post-title {
  color: #4154f1;
}

.recent-blog-posts .post-box:hover .post-img img {
  transform: rotate(6deg) scale(1.2);
}
</style>
