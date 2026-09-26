(() => {
  const menuButton = document.querySelector('#alt-menu-button');
  const drawer = document.querySelector('#alt-drawer');
  const closeButton = drawer?.querySelector('.alt-drawer-close');
  if (!menuButton || !drawer || !closeButton) return;

  const openMenu = () => {
    drawer.showModal();
    menuButton.setAttribute('aria-expanded', 'true');
    menuButton.setAttribute('aria-label', 'Close menu');
    closeButton.focus();
  };

  const closeMenu = () => drawer.close();

  menuButton.addEventListener('click', () => {
    if (drawer.open) closeMenu();
    else openMenu();
  });
  closeButton.addEventListener('click', closeMenu);
  drawer.addEventListener('click', (event) => {
    if (event.target === drawer) closeMenu();
  });
  drawer.addEventListener('close', () => {
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Open menu');
    menuButton.focus();
  });
})();
