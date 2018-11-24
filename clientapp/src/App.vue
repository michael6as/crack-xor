<template>
  <div id="app">
    <div class="form-wrapper">
      <span>
        <textarea v-model="message" v-validate="'required'" placeholder="Enter the encrypted text here" />
          Please Select the key size: 
        <select v-model="keySize">          
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </select>
        </span>      
        <span class="execute-btn" @click="execute">Crack</span>          
        <div class="key-options" v-if="possibleKeys.length > 0">
          <div class="header-md">Possible Keys:</div>
          <span class="key-holder" v-for="key in possibleKeys">{{key}}</span>
        </div>
    </div>    
  </div>
</template>

<script>

import axios from 'axios'

const myApi = axios.create({
  baseURL: 'http://localhost:5000/',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
})

export default {
  name: 'App',
  data () {
    return {
      message: '',
      keySize: '',
      possibleKeys: []
    }
  },
  methods:{
      execute: function() {
        let ascii_arr = this.message.split(',');
        myApi.post('crack', {'text': ascii_arr, 'keySize': this.keySize})
        .then(res => {
          this.possibleKeys = res.data
          })
        }
      }      
}
</script>

<style lang="scss">
html,body{
  height: 100%;
  width:100%;
  margin:0;
  padding:0;
}

#app {
  font-family: OpenSans, 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height:100%;
  display: flex;
  align-items: center;
}

.form-wrapper {
  height: 50%;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}

textarea{
  height: 50%;
  width: 100%;  
  border-radius: 5px;
  box-shadow: 0 1px 6px 0 rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  border: solid 1px #e6e9f2;
  padding-left:12px;
  margin-bottom:12px;
  font-size: 12px;
}

select {
  width: 10%;
}

textarea::placeholder{
  color: #a5a8b5;
}

.header-md{
  font-size: 16px;
  font-weight: bold;
}

.execute-btn{
            float: right;
            width: 100px;
            height: 40px;
            border-radius: 4px;
            font-size: 13px;
            line-height: 1;
            color:#fff;
            display:flex;
            align-items: center;
            justify-content: center;
            background-color: #514fd2;
            margin-right: 20px;
        }

.key-holder {
  padding:1%;
  display:inline-block;
  box-shadow: 0 1px 1px 0 rgba(0.1, 0, 0, 0.1);
}

.key-options {
  border-radius: 5px;
  float: left;
  margin: 5px;
  margin-top: 5%;
  height: 50%;
  overflow: auto;
  font-family: 'Reenie Beanie', arial, serif;
  background-color: #d8d8d8;
  box-shadow: 0 1px 6px 0 rgba(0, 0, 0, 0.1);
  padding:3%;
}
</style>
