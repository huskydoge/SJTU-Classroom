<template>
  <h1>CodingStartup</h1>
</template>

<script lang="ts">

const h1 = document.querySelector("h1");
// h1.innerHTML = h1.textContent.replace(/\S/g, "<span>$&</span>")

// Support Space:
h1.innerHTML = h1.textContent
    .replace(/\S/g, "<span>$&</span>")
    .replace(/\s/g, "<span>&nbsp;</span>");

// [\s]表示，只要出现空白就匹配
// [\S]表示，非空白就匹配

let delay = 0;
document.querySelectorAll("span").forEach((span, index) => {
  delay += 0.1;

  if (index === 6) delay += 0.3;

  span.style.setProperty("--delay", `${delay}s`);
});

h1.addEventListener("animationend", (e) => {
  if (e.target === document.querySelector("h1 span:last-child")) {
    h1.classList.add("ended");
  }
});

</script>

<style lang="scss">
:root {
  font-size: 20px;
}

body {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

h1 {
  font-size: 6rem;
  margin: 0;
  padding: 0;
  font-family: monospace;
  position: relative;
}

h1::after {
  content: "";
  display: inline-block;
  position: absolute;
  width: 20px;
  height: 6rem;
  background-color: #000;
  border-radius: 2px;
  right: -30px;
}

h1.ended::after {
  animation: 1.1s cursor steps(2, jump-none) infinite;
}

@keyframes cursor {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

h1 span {
  /* 	--delay: 10s; */

  display: inline-block;
  overflow: hidden;
  width: 0ch;
  animation: 0.1s text-in ease-in-out forwards;
  animation-delay: var(--delay);
}

@keyframes text-in {
  from {
    width: 0ch;
  }
  to {
    width: 1ch;
  }
}

</style>