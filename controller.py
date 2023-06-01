import model
import view
import text




def start():
    while True:
        choice=view.main_menu()


        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_successful)
            case 2:
                model.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb=model.get_pb()
                view.print_contacts(pb, text.pb_empty)
            case 4:
                contact=view.input_contact(text.input_new_contact)
                name=model.add_contact(contact)
                view.print_message(text.new_contact_succesful(name))
            case 5:
                key_word=view.input_search(text.input_search)
                result=model.search_contact(key_word)
                view.print_contacts(result, error=text.empty_search)
            case 6:
                key_word=view.input_search(text.input_change)
                result=model.search_contact(key_word)
                if len(result)!=1:
                    pass#view.print_contacts()
                else:
                    current_id=result[0].get('id')
                    new_contact=view.input_contact(text.change_contact)
                    name=model.change_contact(new_contact, current_id)
                    

            case 7:
                pass
            case 8:
                break