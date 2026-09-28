css = """
/* Premium Card Styles from Shop (Synced for Homepage) */
.rawwish-card {
    background: var(--rw-white);
    border-radius: 0px; /* Editorial style */
    overflow: hidden;
    font-family: var(--font-sans);
    display: flex;
    flex-direction: column;
    border: 1px solid var(--rw-border);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.rawwish-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
}

.rawwish-card-img-wrap {
    position: relative;
    padding-top: 100%; /* 1:1 aspect for shop */
    background: var(--rw-cream);
    display: block;
    overflow: hidden;
}
.rawwish-card-img-wrap img {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}
.rawwish-card:hover .rawwish-card-img-wrap img {
    transform: scale(1.04);
}

.badge-top-left {
    position: absolute;
    top: 10px; left: 10px;
    background: rgba(255, 255, 255, 0.95);
    color: var(--rw-ink);
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.65rem;
    font-weight: 700;
    display: flex; align-items: center; gap: 4px;
    backdrop-filter: blur(4px);
    z-index: 2;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    transition: all 0.2s ease;
}
.badge-top-left:hover {
    background: var(--rw-plum-dark);
    color: #fff;
    transform: translateY(-2px);
}

.badge-top-right {
    position: absolute;
    top: 10px; right: 10px;
    background: #fff;
    color: #333;
    width: 30px; height: 30px;
    border-radius: 50%;
    display: flex; justify-content: center; align-items: center;
    border: none; cursor: pointer;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    z-index: 2;
    transition: all 0.2s;
    font-size: 0.85rem;
}
.badge-top-right:hover {
    color: var(--rw-rose);
    transform: scale(1.05);
}

.rawwish-card-body {
    padding: 16px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}

.rawwish-title {
    font-family: var(--font-serif);
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--rw-ink);
    margin-bottom: 6px;
    text-decoration: none;
    line-height: 1.2;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
a.rawwish-title-link { text-decoration: none; }
a.rawwish-title-link:hover .rawwish-title { color: var(--rw-plum); }

.rawwish-reviews {
    display: flex; align-items: center; gap: 4px; font-size: 0.75rem; margin-bottom: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--rw-border);
}
.rawwish-reviews .bi-star-fill { color: #F5A623; }

/* Variants inside card */
.variant-label { font-size: 0.7rem; font-weight: 600; text-transform: uppercase; color: var(--rw-muted); margin-bottom: 6px; letter-spacing: 0.05em; }
.variant-grid { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 15px; }
.v-box input { display: none; }
.v-label-pill {
    padding: 4px 10px;
    border: 1px solid var(--rw-border);
    border-radius: 20px;
    font-size: 0.7rem;
    cursor: pointer;
    background: #fff;
    color: var(--rw-ink);
    transition: all 0.2s;
}
.v-box input:checked + .v-label-pill {
    background: var(--rw-plum);
    color: #fff;
    border-color: var(--rw-plum);
}
.v-label-pill:hover { border-color: var(--rw-plum); }

/* Price & Qty Row */
.price-qty-row {
    display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 15px;
}
.price-main {
    font-size: 1.2rem; font-weight: 700; color: var(--rw-ink); font-family: var(--font-sans);
}
.price-tax { font-size: 0.65rem; color: var(--rw-muted); margin-top: -2px; }

.qty-selector {
    display: flex; align-items: center; border: 1px solid var(--rw-border); border-radius: 20px; overflow: hidden; height: 32px; background: #fff;
}
.qty-btn {
    border: none; background: transparent; width: 28px; height: 100%; display: flex; justify-content: center; align-items: center; cursor: pointer; color: var(--rw-ink); font-size: 1rem;
}
.qty-btn:hover { background: var(--rw-cream); }
.qty-input {
    width: 30px; border: none; text-align: center; font-size: 0.85rem; font-weight: 600; padding: 0; pointer-events: none;
}
.qty-input:focus { outline: none; }

/* Add to Cart Button */
.btn-add-cart-dark {
    width: 100%;
    padding: 10px;
    background: var(--rw-ink);
    color: #fff;
    border: none;
    border-radius: 0px;
    font-weight: 600;
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    display: flex; align-items: center; justify-content: center; gap: 8px;
    transition: background 0.3s;
}
.btn-add-cart-dark:hover { background: var(--rw-plum); }
.btn-add-cart-dark:disabled { background: #ccc; cursor: not-allowed; }
"""
with open('static/main/css/rawwish.css', 'a') as f:
    f.write(css)
