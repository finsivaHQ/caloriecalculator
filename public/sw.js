self.addEventListener("install", (e) => {
  self.skipWaiting();
});

self.addEventListener("activate", (e) => {
  // Take control immediately
  e.waitUntil(clients.claim());
});

self.addEventListener("fetch", (e) => {
  // Let the browser handle fetches natively (Network-first), this is just a dummy to enable PWA install prompt.
  return;
});
