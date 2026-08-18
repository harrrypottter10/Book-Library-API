import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Book Library",
    page_icon="📚",
    layout="wide"
)


# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("📚 Book Library")

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Home",
        "➕ Add Book",
        "📖 View Books",
        "🔍 Find Book",
        "✏️ Update Book",
        "🗑️ Delete Book"
    ]
)


# -------------------------------
# Home
# -------------------------------

if menu == "🏠 Home":

    st.title("📚 Book Library")

    st.subheader("Welcome!")

    st.write(
        "Manage your books using this simple Book Library application."
    )



# -------------------------------
# Add Book
# -------------------------------

elif menu == "➕ Add Book":

    st.title("➕ Add Book")

    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")

    year = st.number_input(
        "Year",
        min_value=1001,
        step=1
    )

    in_stock = st.checkbox(
        "In Stock",
        value=False
    )

    if st.button("Add Book"):

        if not title or not author or not genre:
            st.warning("Please fill all fields.")

        else:

            data = {
                "title": title,
                "author": author,
                "genre": genre,
                "year": year,
                "in_stock": in_stock
            }

            response = requests.post(
                f"{API_URL}/",
                json=data
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Book added successfully!")

                st.write(
                    f"Book ID: `{result['id']}`"
                )

            else:

                st.error(response.text)


# -------------------------------
# View Books
# -------------------------------

elif menu == "📖 View Books":

    st.title("📖 All Books")

    if st.button("Load Books"):

        response = requests.get(
            f"{API_URL}/"
        )

        if response.status_code == 200:

            books = response.json()

            if not books:

                st.info("No books found.")

            else:

                for book in books:

                    st.subheader(
                        f"📖 {book['title']}"
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        st.write(
                            f"**Author:** {book['author']}"
                        )

                        st.write(
                            f"**Genre:** {book['genre']}"
                        )

                    with col2:

                        st.write(
                            f"**Year:** {book['year']}"
                        )

                        if book["in_stock"]:

                            st.success(
                                "**In Stock:** ✅ Yes"
                            )

                        else:

                            st.error(
                                "**In Stock:** ❌ No"
                            )

                    st.caption(
                        f"ID: {book['id']}"
                    )

                    st.divider()

        else:

            st.error(response.text)


# -------------------------------
# Find Book
# -------------------------------

elif menu == "🔍 Find Book":

    st.title("🔍 Find Book")

    book_id = st.text_input(
        "Enter Book ID"
    )

    if st.button("Find Book"):

        if not book_id:

            st.warning("Please enter a Book ID.")

        else:

            response = requests.get(
                f"{API_URL}/{book_id}"
            )

            if response.status_code == 200:

                book = response.json()

                st.subheader(
                    f"📖 {book['title']}"
                )

                st.write(
                    f"**Author:** {book['author']}"
                )

                st.write(
                    f"**Genre:** {book['genre']}"
                )

                st.write(
                    f"**Year:** {book['year']}"
                )

                if book["in_stock"]:

                    st.success(
                        "In Stock: Yes ✅"
                    )

                else:

                    st.error(
                        "In Stock: No ❌"
                    )

            else:

                st.error(
                    response.text
                )


# -------------------------------
# Update Book
# -------------------------------

elif menu == "✏️ Update Book":

    st.title("✏️ Update Book")

    book_id = st.text_input(
        "Book ID"
    )

    title = st.text_input(
        "New Title"
    )

    author = st.text_input(
        "New Author"
    )

    genre = st.text_input(
        "New Genre"
    )

    year = st.number_input(
        "New Year",
        min_value=1001,
        step=1
    )

    in_stock = st.checkbox(
        "In Stock",
        value=False
    )

    if st.button("Update Book"):

        if not book_id:

            st.warning(
                "Please enter the Book ID."
            )

        else:

            data = {
                "title": title,
                "author": author,
                "genre": genre,
                "year": year,
                "in_stock": in_stock
            }

            response = requests.put(
                f"{API_URL}/{book_id}",
                json=data
            )

            if response.status_code == 200:

                st.success(
                    "Book updated successfully!"
                )

            else:

                st.error(
                    response.text
                )


# -------------------------------
# Delete Book
# -------------------------------

elif menu == "🗑️ Delete Book":

    st.title("🗑️ Delete Book")

    book_id = st.text_input(
        "Enter Book ID"
    )

    if st.button("Delete Book"):

        if not book_id:

            st.warning(
                "Please enter a Book ID."
            )

        else:

            response = requests.delete(
                f"{API_URL}/{book_id}"
            )

            if response.status_code == 200:

                st.success(
                    "Book deleted successfully!"
                )

            else:

                st.error(
                    response.text
                )