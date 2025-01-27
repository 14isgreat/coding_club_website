function copyCode(button) {
    const codeBlock = button.parentElement.querySelector('code');
    const textToCopy = codeBlock.textContent;

    navigator.clipboard.writeText(textToCopy).then(() => {
      button.textContent = "Copied!";
      setTimeout(() => {
        button.textContent = "Copy";
      }, 2000);
    }).catch(err => {
      console.error('Failed to copy text: ', err);
    });
  }