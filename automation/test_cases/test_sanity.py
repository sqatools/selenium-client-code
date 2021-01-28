from automation.data.test_variables import *
from time import sleep

def test_logbook_1(setup):
    setup.olb.add_log_book_event(log_book_1)
    sleep(5)
    setup.olb.verify_new_logbook_msg(log_book_1['event_msg'])

# def test_lo_book_2(setup):
#     setup.op.add_log_book_event(log_book_2)
#     sleep(5)

# def test_create_orp(setup):
#     setup.orp.create_operator_round_planning(orp1)
#     sleep(5)

# def test_stading_order(setup):
#     setup.so.create_standing_order(st_orders_1)
#     sleep(10)

# def test_work_instructions(setup):
#     setup.wi.create_work_instruction(wi_instructions)
#     sleep(10)