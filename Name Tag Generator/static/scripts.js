document.getElementById("csp-good").addEventListener("click", () => {
    document.getElementById("csp").value = "default-src 'self'";
    //document.getElementById("csp-form").submit();
  });
  
  document.getElementById("csp-bad-unsafe-inline").addEventListener("click", () => {
    document.getElementById("csp").value = "default-src 'self' 'unsafe-inline'";
    //document.getElementById("csp-form").submit();
  });
  
  document.getElementById("csp-bad-unsafe-eval").addEventListener("click", () => {
    document.getElementById("csp").value = "default-src 'self' 'unsafe-inline' 'unsafe-eval'";
    //document.getElementById("csp-form").submit();
  });
  
  document.getElementById("xss-payload-1").addEventListener("click", () => {
    document.getElementById("name").value = document.getElementById("name").value + '<img src="x" onerror="alert(\'Wombats Rule!\');">';
  });
  
  document.getElementById("xss-payload-2").addEventListener("click", () => {
    document.getElementById("name").value = document.getElementById("name").value + '<img src="x" onerror="console.log(\'Yubikey for life! cccccbgftciniejiltjedvgbcukjkrbifdtcubdrevrc!\');"></img>';
  });
  document.getElementById("xss-payload-3").addEventListener("click", () => {
    document.getElementById("name").value = document.getElementById("name").value + 'Crypto? More like Crypt-Oh-no!<img src="x" onerror="ethereum.request({ method: \'eth_requestAccounts\' });"></img>';
  });
  
  
  function createConfetti() {
    const output = document.getElementById("namebox");
  
    if (output) {
      const outputRect = output.getBoundingClientRect();
      const leftX = outputRect.left / window.innerWidth;
      const rightX = outputRect.right / window.innerWidth;
      const centerY = (outputRect.top + outputRect.bottom) / 2 / window.innerHeight;
  
      const confettiSettingsLeft = {
        particleCount: 50,
        spread: 60,
        startVelocity: 30,
        angle: 40,
        origin: { x: leftX, y: centerY },
      };
  
      const confettiSettingsRight = {
        particleCount: 50,
        spread: 60,
        startVelocity: 30,
        angle: 140,
        origin: { x: rightX, y: centerY },
      };
  
      confetti(confettiSettingsLeft);
      confetti(confettiSettingsRight);
    }
  }
  
  
  
  
  document.getElementById("name-submit").addEventListener("click", () => {
    
    const output = document.getElementById("namebox");
    const nameInput = document.getElementById("name");
    const nameValue = nameInput.value;
    if (nameValue && output) {
      output.innerHTML = `${nameValue}`;
      createConfetti();
  
      // Update the URL with the name parameter without reloading the page
      const url = new URL(window.location.href);
      url.searchParams.set("name", nameValue);
      window.history.pushState({}, "", url);
    }
  });
  
  