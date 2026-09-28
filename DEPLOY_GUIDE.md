# Raw Wish: VPS Deployment & Data Migration Guide

This guide is meant for internal use to help you move your exact localhost database (with all the products, variants, and categories) and all uploaded images directly to your VPS.

## 1. Exporting Your Local Database
Instead of re-running seed scripts and hoping everything matches, the safest and most exact way to copy your data is to create a JSON dump of your local database.

Run this command on your **local machine** inside the `Rawwish` directory:
```bash
../venv/bin/python manage.py dumpdata --exclude auth.permission --exclude contenttypes > rawwish_datadump.json
```
*This creates a `rawwish_datadump.json` file containing all your local data.*

## 2. Transferring Files to the VPS
You need to transfer your code, the datadump, and most importantly, your `media/` folder (which contains all the product/category images).

Using `scp` (or your preferred SFTP tool like FileZilla):
```bash
# Upload the database dump
scp rawwish_datadump.json user@your_vps_ip:/path/to/remote/Rawwish/

# Upload the entire media folder
scp -r media/ user@your_vps_ip:/path/to/remote/Rawwish/
```

## 3. Setting Up the VPS
SSH into your VPS and navigate to the project directory:
```bash
ssh user@your_vps_ip
cd /path/to/remote/Rawwish/
```

Create and activate a virtual environment, then install the dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 4. Initializing the Remote Database & Loading Data
Run migrations to set up the empty database tables, and then load the JSON dump you uploaded:

```bash
# Set up empty tables
python manage.py migrate

# Load your exact local data into the remote DB
python manage.py loaddata rawwish_datadump.json
```

## 5. Final Steps
Collect static files so your CSS and JS load properly:
```bash
python manage.py collectstatic --noinput
```

Ensure your `media/` folder has the correct permissions so your web server (like Nginx/Gunicorn) can read the images:
```bash
chmod -R 755 media/
```

You are now ready to start your production server! Your VPS will look exactly like your local machine, complete with all images and product variants.
