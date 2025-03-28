import streamlit as st
from library import Library
from storage import load_library, save_library


lib = Library()
lib.books = load_library()

st.title("📚 Personal Library Manager")

menu = ["Add Book", "Remove Book", "Search Books", "Display All", "Statistics"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1800, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.radio("Have you read this book?", ["Yes", "No"]) == "Yes"

    if st.button("Add Book"):
        msg = lib.add_book(title, author, year, genre, read_status)
        save_library(lib.books)
        st.success(msg)

elif choice == "Remove Book":
    st.subheader("❌ Remove a Book")
    title = st.text_input("Enter book title to remove")
    
    if st.button("Remove"):
        msg = lib.remove_book(title)
        save_library(lib.books)
        st.warning(msg)

elif choice == "Search Books":
    st.subheader("🔍 Search for a Book")
    search_type = st.radio("Search by", ["Title", "Author"])
    query = st.text_input("Enter search term")

    if st.button("Search"):
        results = lib.search_books(query, by="title" if search_type == "Title" else "author")
        if results:
            for book in results:
                st.write(f'📖 *{book["title"]}* by {book["author"]} ({book["year"]}) - {book["genre"]} - {"✅ Read" if book["read_status"] else "❌ Unread"}')
        else:
            st.warning("No books found.")

elif choice == "Display All":
    st.subheader("📖 Your Library")
    books = lib.get_books()
    
    if books:
        for book in books:
            st.write(f'📖 *{book["title"]}* by {book["author"]} ({book["year"]}) - {book["genre"]} - {"✅ Read" if book["read_status"] else "❌ Unread"}')
    else:
        st.info("Library is empty.")

elif choice == "Statistics":
    st.subheader("📊 Library Statistics")
    total, percentage = lib.get_statistics()
    st.write(f"📚 *Total Books:* {total}")
    st.write(f"✅ *Percentage Read:* {percentage}%")

st.sidebar.markdown("---")
st.sidebar.info("Developed using Python & Streamlit")