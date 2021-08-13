function detectMob() {
    return window.innerWidth < 768;
}
const isMobile = detectMob()


export { isMobile }