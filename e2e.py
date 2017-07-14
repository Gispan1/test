import modules.session as session_module

def purchase_runner(item_name="dvd player"):
    website = session_module.amazon()
    website.open_amzon_site()
    website.search_items(item_name)
    website.add_items_to_cart(max_amount=500)
    website.proceed_to_checkout()
    website.fill_user_details('automation_user','automation_user@malinator.com','somepassword')
    website.end_session()

def content_scraping_runner():
    website = session_module.perimeterx()
    website.open_perimeterx_site()
    website.get_all_pages()
    website.end_session()