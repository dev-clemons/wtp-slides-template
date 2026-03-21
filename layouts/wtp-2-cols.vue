<template>
  <div class="custom-layout">
    <div class="content slidev-layout" :style="{ width: leftWidth }">
      <slot />
    </div>
    <div class="iframe-container" :style="{ width: 'calc(100% - ' + leftWidth + ')' }">
      <div style="position: absolute;transform: scale(0.66); transform-origin: 0 0; width: 150%; height: 150%;">
        <iframe :src="url.href" :style="{position: 'absolute',width: 'calc(100% - ' + leftWidth + ')', height: '100%'}" allow="usb;clipboard-write"></iframe>
      </div>div>
    </div>
  </div>
</template>

<script setup>
import LZString from "lz-string";
const props = defineProps({
  base: {
    type: String,
    required: false
  },
  code: {
    type: String,
    required: true,
  },
  leftWidth: {
    type: String,
    default: '45%',
  },
  device: {
    type: String,
    default: '-'
  },
  wtpLayout: {
    type: String,
    default: ''
  },
  playground: {
    type: String,
    default: ''
  }
  
});

function encodeInputCode(inputCode) {
    const codeObject = [{ name: "main.py", data: inputCode }] // step 1
    const jsonString = JSON.stringify(codeObject); // step 2
    const base64compressed = LZString.compressToBase64(jsonString) // step 3 and 4
    return base64compressed; // step 5
}

let base = "https://webtigerpython.ethz.ch"
if(props.base){
  base = props.base
}
let encodedCode = encodeInputCode(props.code)
let url = new URL(base);
if(props.playground){
  console.log(props.playground)
  url.searchParams.append("playground", props.playground)
}
url.searchParams.append("code", encodedCode);
url.searchParams.append("device", props.device)
if(props.wtpLayout){
  url.searchParams.append("layout", props.wtpLayout)
}
console.log(url.href)
</script>

<style>
.custom-layout {
  display: flex;
  height: 100vh; /* Full height of the viewport */
}

</style>
