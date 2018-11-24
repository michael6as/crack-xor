<template>
  <div class="crack-form-wrapper">      
  </div>
</template>

<script>

import {mapMutations,mapState} from 'vuex'
import axios from 'axios'

export default {
  data () {
    return {
      message,
      keySize,
      possibleKeys
    }
  },
  computed: {
    balance: function() {
        return this.getUserInfo(this.ctrlName)
    }
  },
  methods:{
      ...mapMutations(['crackMyCipher']),
      execute: function() {
        axios.post('http:localhost:5000/crack', {'text': message, 'keySize': keySize})
        .then(res=> function(){
          possibleKeys = res.data
          })
        }
      }      
}
</script>

<style lang="scss" scoped>
.apps-panel-wrapper{
  flex:0 0 70px;
  background-color: #454c68;
  box-shadow: 0 0 8px 0 rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 20px;
}

.app-panel-item{
    width:40px;
    height:40px;
    border-radius: 50%;
    background-color: rgba(255, 255, 255, 0.2);
    margin-bottom: 25px;
    display:flex;
    align-items: center;
    justify-content: center;

    &.selected{
        background-color: #47a0f9;
        border: solid 1px #459bf3;
    }

    //cuz images are bad
    img{
        margin-left: 4px;
        margin-top:5px;
    }
}
</style>
