# 🧩 PROMPT SYSTEM: MODULAR IMAGE GENERATION ENGINE
**Mục tiêu: 200+ ảnh | Phương pháp: Base DNA + 6 Slot biến số xoay vòng**
*File: `projects/008/prompt_system.md` | Phong cách gốc: `projects/008/style.md`*

---

## 📐 CÔNG THỨC PROMPT

```
[BASE DNA] + [SLOT A: Character] + [SLOT B: Costume] + [SLOT C: Creature] + [SLOT D: Action] + [SLOT E: Environment] + [SLOT F: Lighting] + [SUFFIX]
```

---

## 🧬 BASE DNA (Giữ nguyên mọi prompt)

```text
cinematic tactile surrealism, dark fantasy editorial fashion photography, 35mm film still, grand mythical pilgrimage across a surreal fantasy realm, striking tri-chromatic color palette of deep matte charcoal-black, crisp bone white, and vibrant scarlet crimson, high contrast, sharp 3D volume, scale inversion with colossal fantastical surreal leviathans and chimeras in close intimate side-by-side companionship with humans, extreme wide cinematic establishing shot, full body composition showing the entire colossal fantasy beast and tall radiant statuesque traveler paired side-by-side fully enclosed within the 16:9 frame with generous margins and no cropping, clean minimalist composition, zero prop clutter,
```

---

## 🧲 SUFFIX (Giữ nguyên mọi prompt)

```text
entire fantasy creature and character fully visible in frame, complete full-body silhouette, side-by-side close companionship, wide margins, sharp focus, 8k photorealistic --ar 16:9 --no distant character, separated character, cropped, out of frame, cut off, framing cutoff, clipped edges, overflowing frame, close-up, zoom in, modern clothing, trousers, coats, jackets, jeans, suit, shiny, gloss, glossy, polished, brass, bronze, copper, chrome, lacquer, reflection, porcelain, ceramic, glaze, glazed, enamel, specular highlights, blurry, washed out, muted, low contrast, hazy, muddy, flat lighting, gray haze, creepy realistic bug hairs, grotesque insect slime, wood carving, puppet, doll, toy, clutter, furniture, carts, wagons, pots, pans, excessive props
```

---

## 🎰 SLOT A: NHÂN VẬT (CHARACTER)

| ID | Prompt Fragment |
|---|---|
| A1 | an ethereally beautiful young woman with delicate symmetrical features, smooth porcelain skin, flowing platinum white hair past her shoulders |
| A2 | an ethereally beautiful young woman with sharp split-tone bob (half black half white), delicate symmetrical features, porcelain skin |
| A3 | a distinguished graceful elder man with a trimmed silver beard, warm deep-set eyes, weathered kind face, dignified artistic presence |
| A4 | a distinguished graceful elder woman with flowing silver-white hair pinned loosely, soft laugh lines, warm serene gaze |
| A5 | a young couple — she with long platinum hair and he with tousled auburn curls, both with serene porcelain features |
| A6 | an elderly couple side by side — he with a trimmed white beard and felt cap, she with braided silver hair and a gentle smile |
| A7 | a solitary young woman seen from behind, long white hair catching the breeze, standing small against a towering landscape |
| A8 | three young women walking together, each with distinct hair (platinum straight, dark curly, copper braids), matching in grace |
| A9 | a child (8-10 years old) with round cheeks and curious wide eyes, short messy auburn hair, barefoot |
| A10 | a teenage girl with freckles across her nose, wavy strawberry-blonde hair, thoughtful sideways glance |
| A11 | a tall slender young man with sharp cheekbones, dark wavy hair to his jaw, quiet intensity in his gaze |
| A12 | a middle-aged woman with streaks of silver in dark hair, strong jawline, reading glasses perched on her nose |

---

## 🎰 SLOT B: TRANG PHỤC SIÊU THỰC (SURREAL COSTUME)

> [!IMPORTANT]
> Mỗi prompt BẮT BUỘC phải có ít nhất 1 yếu tố trang phục siêu thực từ pool này.

| ID | Prompt Fragment |
|---|---|
| B1 | wearing a mushroom-membrane cape draped over a tiered ivory linen dress, with living moss growing along the hem |
| B2 | wearing a bark-plated corset with natural crack patterns over flowing petal-layered skirt of dried magnolia petals |
| B3 | wearing seed-pod epaulettes sprouting from a raw linen coat, cocoon-wrapped sleeves, root-laced boots |
| B4 | wearing a moth-wing shawl with translucent veined panels over a hand-woven hemp dress, lichen collar |
| B5 | wearing a caterpillar-quilted vest (red-white segmented stitching) over balloon puff-sleeve linen blouse |
| B6 | wearing a full-length spore-dusted cape made of pressed dried mushroom sheets, felted wool trousers underneath |
| B7 | wearing an oversized petal-collar coat (stiff dried sunflower petals forming the collar), raw wool underneath |
| B8 | wearing a woven-reed chest plate over layered rust-dyed linen, shoulder pieces carved from dried seed husks |
| B9 | wearing a cocoon-silk wrap dress that spirals around the body, one arm bare, fern-frond wristband |
| B10 | wearing a Pierrot-style cream suit with mushroom-cap buttons and a collar encrusted with dried lichen patches |
| B11 | wearing layered felted wool in ochre and cream, with a living vine belt and dangling dried berry clusters |
| B12 | wearing a sculptural overcoat made entirely of overlapping dried leaves pressed flat, hemp rope closure |
| B13 | wearing a tattered hand-stitched patchwork robe of mismatched natural fabrics (linen, raw silk, bark-cloth) |
| B14 | wearing a flowing ivory gown with fungal-shelf shoulders (bracket fungus growing horizontally from each shoulder) |
| B15 | wearing a snail-shell-shaped helmet and a quilted linen jumpsuit with root-lace detailing down the legs |

---

## 🎰 SLOT C: SINH THỂ (CREATURE)

| ID | Prompt Fragment |
|---|---|
| C1 | a colossal weathered ladybug with cracked lacquer red-and-white shell, exposed aged timber leg joints, rustic leather saddle |
| C2 | a colossal white porcelain ant with red speckles, matte ceramic body, carrying a wooden bakery kitchen with smoking clay chimney on its back |
| C3 | a colossal white porcelain praying mantis carrying a traveling instrument collection: felt-wrapped horns, violin cases, woven bundles strapped with hemp rope |
| C4 | a colossal walking snail with its shell sculpted into a multi-story dwelling — curved wooden windows, fabric awnings, hanging fern pots, a tiny staircase |
| C5 | a colossal bumblebee-moth with fuzzy thorax and translucent veined wings, spiraling warm tungsten filament lights (2200K) wrapped around its body |
| C6 | a colossal obsidian-black stag beetle with a matte shell, curved horn mandibles, weathered iron joint plates |
| C7 | a colossal grasshopper with riveted iron-patina head plates, canvas-membrane wings, carrying rolled red blankets and herb satchels |
| C8 | a colossal friendly caterpillar perched on a gnarled tree branch, segmented body with hand-stitched quilted red-white-black stripes, twig antennae |
| C9 | a colossal dragonfly hovering mid-air, iridescent matte wings like stained glass, dried-flower garlands trailing from its tail |
| C10 | a colossal moth resting on a mushroom cap, dusty powder-blue wings with eyespot patterns, soft fur collar, carrying a tiny lantern |
| C11 | a colossal pill bug (roly-poly) uncurled halfway, armored plates of cracked gray ceramic, carrying woven baskets in the gaps between plates |
| C12 | a colossal scarab beetle with carved wooden shell panels instead of chitin, pulling a small wooden cart loaded with mushrooms |

---

## 🎰 SLOT D: HÀNH ĐỘNG (ACTION / INTERACTION)

| ID | Prompt Fragment |
|---|---|
| D1 | riding on the creature's back, one hand resting on a leather harness, gazing ahead at the misty path |
| D2 | walking alongside the creature on a forest trail, carrying a woven basket of wild herbs |
| D3 | sitting cross-legged on a mossy log, pouring tea from a clay kettle into a crackle-glaze ceramic cup |
| D4 | leaning against the creature's leg, reading a cloth-bound book, one hand absently stroking its shell |
| D5 | standing on a wooden balcony built into the creature's shell, looking out at the landscape below |
| D6 | playing a felt-wrapped trumpet, eyes closed, body swaying slightly to the melody |
| D7 | reaching up to touch a towering mushroom cap, fingers grazing its surface, tiny spores drifting down |
| D8 | kneeling on damp moss, arranging dried flowers and mushrooms into a small offering circle |
| D9 | lying in a hammock strung between two giant mushroom stems, one foot dangling, half-asleep |
| D10 | standing at the edge of a cliff overlooking a valley of enormous mushrooms, wind catching her hair |
| D11 | braiding the creature's antennae with dried wildflowers, sitting on its head with legs dangling |
| D12 | stirring a cast-iron pot hung over a small campfire, steam rising, the creature resting behind her |
| D13 | dancing barefoot on a mushroom cap the size of a stage, arms outstretched, spinning slowly |
| D14 | writing in a leather journal at a wooden desk built into a hollow mushroom trunk |
| D15 | hanging laundry on a line strung between two giant mushroom stems, white linen sheets catching the breeze |
| D16 | feeding the creature from her palm — tiny mushrooms and dried berries |
| D17 | walking across a rope bridge between two giant mushroom canopies, holding the hemp rope rail |
| D18 | curled up inside a giant curled leaf, using it as a natural sleeping pod, blanket of dried petals |
| D19 | harvesting bracket fungus from a colossal tree trunk with a small bone-handled knife |
| D20 | leading a procession of three different creatures along a winding forest path, carrying a lantern |

---

## 🎰 SLOT E: BỐI CẢNH (ENVIRONMENT)

| ID | Prompt Fragment |
|---|---|
| E1 | towering colossal red Amanita muscaria mushrooms filling the background like ancient trees, damp mossy forest floor |
| E2 | a dense canopy of brown and cream oyster mushrooms growing from enormous fallen logs, morning dew on everything |
| E3 | a vast open meadow with scattered colossal mushrooms in the distance, waist-high wild grass and dried seed heads |
| E4 | inside a hollow mushroom trunk converted into a cozy dwelling — wooden shelves, hanging herbs, a cot with quilted blankets |
| E5 | at the edge of a still forest pond reflecting the enormous red mushroom canopy above, lily pads and reeds |
| E6 | a rocky hillside with mushrooms growing from crevices, a winding stone path, distant mountains in haze |
| E7 | a forest clearing after rain, puddles reflecting the overcast sky, mushroom caps glistening with water droplets |
| E8 | an autumn forest floor blanketed in golden and rust-colored fallen leaves, mushrooms pushing through the leaf litter |
| E9 | a moss-covered stone bridge arching over a narrow stream, giant mushrooms framing both sides |
| E10 | the interior of a colossal snail shell repurposed as a multi-room dwelling, warm light spilling from small round windows |
| E11 | a terraced mushroom garden on a hillside — different mushroom species on each level, connected by wooden steps |
| E12 | a twilight forest with the last light filtering through mushroom canopies, creating long orange-pink shadows |
| E13 | a windswept coastal cliff where mushrooms grow sideways from the rock face, ocean fog rolling in below |
| E14 | a canopy-level view from atop a mushroom cap, looking down at the forest floor far below, other caps at eye level |
| E15 | a frozen winter forest with mushrooms dusted in fresh snow, bare branches, breath visible in cold air |

---

## 🎰 SLOT F: ÁNH SÁNG (LIGHTING)

| ID | Prompt Fragment |
|---|---|
| F1 | soft diffused overcast daylight (6500K), gentle even illumination, no harsh shadows |
| F2 | warm golden hour side-lighting from a low sun, long shadows across mossy ground |
| F3 | dappled light filtering through mushroom canopy gaps, creating patterns of light and shadow on the subject |
| F4 | moody overcast dusk atmosphere, deep blue-grey sky, warm tungsten glow (2200K) from small lanterns |
| F5 | flat bright noon daylight under cloud cover, minimal shadows, colors at full saturation |
| F6 | backlit — subject silhouetted against a bright misty background, rim light outlining their figure |
| F7 | campfire-adjacent warm light from below, flickering orange on faces, deep shadows behind |
| F8 | early morning fog with diffused pale pink-orange light, everything softened and slightly hazy |

---

## 🔧 CÁCH GHÉP PROMPT

### Công thức hoàn chỉnh:
```
[BASE DNA], [SLOT A], [SLOT B], [SLOT C], [SLOT D], [SLOT E], [SLOT F], [SUFFIX]
```

### 10 VÍ DỤ COMBO:

**Combo 1** → A1 + B1 + C1 + D1 + E1 + F1
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, an ethereally beautiful young woman with delicate symmetrical features, smooth porcelain skin, flowing platinum white hair past her shoulders, wearing a mushroom-membrane cape draped over a tiered ivory linen dress, with living moss growing along the hem, riding on the back of a colossal weathered ladybug with cracked lacquer red-and-white shell, exposed aged timber leg joints, rustic leather saddle, gazing ahead at the misty path, towering colossal red Amanita muscaria mushrooms filling the background like ancient trees, damp mossy forest floor, soft diffused overcast daylight (6500K), gentle even illumination, no harsh shadows, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 2** → A3 + B6 + C3 + D6 + E7 + F4
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, a distinguished graceful elder man with a trimmed silver beard, warm deep-set eyes, weathered kind face, dignified artistic presence, wearing a full-length spore-dusted cape made of pressed dried mushroom sheets, felted wool trousers underneath, beside a colossal white porcelain praying mantis carrying a traveling instrument collection: felt-wrapped horns, violin cases, woven bundles strapped with hemp rope, playing a felt-wrapped trumpet, eyes closed, body swaying slightly to the melody, a forest clearing after rain, puddles reflecting the overcast sky, mushroom caps glistening with water droplets, moody overcast dusk atmosphere, deep blue-grey sky, warm tungsten glow (2200K) from small lanterns, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 3** → A2 + B2 + C8 + D4 + E8 + F3
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, an ethereally beautiful young woman with sharp split-tone bob (half black half white), delicate symmetrical features, porcelain skin, wearing a bark-plated corset with natural crack patterns over flowing petal-layered skirt of dried magnolia petals, leaning against a colossal friendly caterpillar perched on a gnarled tree branch, segmented body with hand-stitched quilted red-white-black stripes, twig antennae, reading a cloth-bound book, one hand absently stroking its shell, an autumn forest floor blanketed in golden and rust-colored fallen leaves, mushrooms pushing through the leaf litter, dappled light filtering through mushroom canopy gaps, creating patterns of light and shadow on the subject, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 4** → A5 + B10 + C4 + D5 + E10 + F1
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, a young couple — she with long platinum hair and he with tousled auburn curls, both with serene porcelain features, he wearing a Pierrot-style cream suit with mushroom-cap buttons and a collar encrusted with dried lichen patches, she wearing a moth-wing shawl with translucent veined panels, standing on a wooden balcony built into the creature's shell, looking out at the landscape below, the interior of a colossal snail shell repurposed as a multi-room dwelling, warm light spilling from small round windows, soft diffused overcast daylight (6500K), gentle even illumination, no harsh shadows, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 5** → A9 + B11 + C12 + D16 + E3 + F2
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, a child (8-10 years old) with round cheeks and curious wide eyes, short messy auburn hair, barefoot, wearing layered felted wool in ochre and cream, with a living vine belt and dangling dried berry clusters, feeding a colossal scarab beetle with carved wooden shell panels instead of chitin from her palm — tiny mushrooms and dried berries, a vast open meadow with scattered colossal mushrooms in the distance, waist-high wild grass and dried seed heads, warm golden hour side-lighting from a low sun, long shadows across mossy ground, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 6** → A7 + B9 + C5 + D10 + E13 + F6
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, a solitary young woman seen from behind, long white hair catching the breeze, standing small against a towering landscape, wearing a cocoon-silk wrap dress that spirals around the body, one arm bare, fern-frond wristband, a colossal bumblebee-moth with fuzzy thorax and translucent veined wings hovering nearby, spiraling warm tungsten filament lights (2200K) wrapped around its body, standing at the edge of a cliff overlooking a valley of enormous mushrooms, wind catching her hair, a windswept coastal cliff where mushrooms grow sideways from the rock face, ocean fog rolling in below, backlit — subject silhouetted against a bright misty background, rim light outlining her figure, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 7** → A4 + B13 + C10 + D3 + E4 + F7
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, a distinguished graceful elder woman with flowing silver-white hair pinned loosely, soft laugh lines, warm serene gaze, wearing a tattered hand-stitched patchwork robe of mismatched natural fabrics (linen, raw silk, bark-cloth), a colossal moth resting on a mushroom cap nearby, dusty powder-blue wings with eyespot patterns, soft fur collar, carrying a tiny lantern, sitting cross-legged on a mossy log, pouring tea from a clay kettle into a crackle-glaze ceramic cup, inside a hollow mushroom trunk converted into a cozy dwelling — wooden shelves, hanging herbs, a cot with quilted blankets, campfire-adjacent warm light from below, flickering orange on face, deep shadows behind, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 8** → A10 + B5 + C9 + D13 + E14 + F8
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, a teenage girl with freckles across her nose, wavy strawberry-blonde hair, thoughtful sideways glance, wearing a caterpillar-quilted vest (red-white segmented stitching) over balloon puff-sleeve linen blouse, a colossal dragonfly hovering mid-air, iridescent matte wings like stained glass, dried-flower garlands trailing from its tail, dancing barefoot on a mushroom cap the size of a stage, arms outstretched, spinning slowly, a canopy-level view from atop a mushroom cap, looking down at the forest floor far below, other caps at eye level, early morning fog with diffused pale pink-orange light, everything softened and slightly hazy, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 9** → A11 + B3 + C6 + D17 + E9 + F3
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, a tall slender young man with sharp cheekbones, dark wavy hair to his jaw, quiet intensity in his gaze, wearing seed-pod epaulettes sprouting from a raw linen coat, cocoon-wrapped sleeves, root-laced boots, a colossal obsidian-black stag beetle with a matte shell following behind, curved horn mandibles, weathered iron joint plates, walking across a rope bridge between two giant mushroom canopies, holding the hemp rope rail, a moss-covered stone bridge arching over a narrow stream, giant mushrooms framing both sides, dappled light filtering through mushroom canopy gaps, creating patterns of light and shadow, shallow depth of field, 8k photorealistic --ar 16:9
```

**Combo 10** → A8 + B7 + C11 + D20 + E11 + F2
```text
cinematic tactile surrealism, photorealistic editorial photography, 35mm film grain, muted earthy natural tones, matte textures throughout, no brass no gleaming metal no shiny surfaces, scale inversion with colossal insects and mushrooms, three young women walking together, each with distinct hair (platinum straight, dark curly, copper braids), matching in grace, each wearing an oversized petal-collar coat (stiff dried sunflower petals forming the collar), raw wool underneath, leading a colossal pill bug (roly-poly) uncurled halfway, armored plates of cracked gray ceramic, carrying woven baskets in the gaps between plates, a terraced mushroom garden on a hillside — different mushroom species on each level, connected by wooden steps, warm golden hour side-lighting from a low sun, long shadows across mossy ground, shallow depth of field, 8k photorealistic --ar 16:9
```

---

## 📊 KHẢ NĂNG TỔ HỢP

| Slot | Số lượng | Mô tả |
|---|---|---|
| A (Character) | 12 | Nhân vật |
| B (Costume) | 15 | Trang phục siêu thực |
| C (Creature) | 12 | Sinh thể |
| D (Action) | 20 | Hành động / tương tác |
| E (Environment) | 15 | Bối cảnh |
| F (Lighting) | 8 | Ánh sáng |

**Tổng tổ hợp lý thuyết:** 12 × 15 × 12 × 20 × 15 × 8 = **5,184,000 prompt**

200 ảnh = chọn 200 combo hay nhất từ biển khả năng.

---

## ⛔ VẬT LIỆU CẤM (MATERIAL BLACKLIST — copy vào mọi prompt)

Đoạn `no brass no gleaming metal no shiny surfaces` trong BASE DNA đã cover.

Nếu AI vẫn sinh ra đồ bóng, thêm negative prompt:
```text
--no brass, bronze, polished metal, gleaming, shiny, glossy, chrome, gold-plated, copper
```
