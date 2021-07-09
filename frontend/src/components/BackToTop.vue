<template>
    <button @click="topFunction()" id="myBtn" title="Go to top">Top</button>
</template>

<script>
export default {
  name: 'BackToTop',
  mounted() {
    //Get the button
    var mybutton = document.getElementById("myBtn");

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            mybutton.style.display = "block";
        } else {
            mybutton.style.display = "none";
        }
    }
  },
  methods: {
    topFunction: function () {        
        // When the user clicks on the button, scroll to the top of the document
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
}

#myBtn {
  display: none;
  position: fixed;
  bottom: 20px;
  right: 30px;
  z-index: 99;
  font-size: 18px;
  border: 1px;
  outline: none;
  background-color: #149ddd;
  color: white;
  cursor: pointer;
  padding: 15px;
  border-radius: 100%;
}

#myBtn:hover {
  background-color: white;
  color: #149ddd;
  border-style: solid;
  border-color: #149ddd;
}
</style>
