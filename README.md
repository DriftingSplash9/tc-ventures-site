# tc-ventures.ca

Hand-written static site. No framework, no build step, no CMS.

```
public/            what gets served
  index.html       home
  projects.html    the graph + rocket lander
  background.html  experience, skills, resume
  404.html
  assets/style.css one stylesheet
  assets/img/      screenshots
wrangler.jsonc     Cloudflare static-assets config
```

Edit the HTML directly and push. Cloudflare deploys on push to `main`.

No JavaScript on the site at all — if a page ever needs some, inline it rather
than adding a bundler.
