# EXAMPLES

## Code Usage

### 1. Initializing Supabase
```javascript
import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm'

const supabaseUrl = 'YOUR_SUPABASE_URL'
const supabaseKey = 'YOUR_SUPABASE_ANON_KEY'
const supabase = createClient(supabaseUrl, supabaseKey)
```

### 2. Form Submission Function
```javascript
async function submitForm(data) {
    const { error } = await supabase
        .from('inquiries')
        .insert({
            full_name: data.name,
            email_address: data.email,
            // ... other fields
        })
    
    if (error) console.error('Error:', error)
    else console.log('Success!')
}
```

### 3. GSAP Animation Trigger
```javascript
gsap.from(".hero-title", {
    duration: 1,
    y: 100,
    opacity: 0,
    ease: "power4.out",
    scrollTrigger: {
        trigger: ".hero-section",
        start: "top center"
    }
});
```
