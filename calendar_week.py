import sublime, sublime_plugin
import datetime

class CalendarWeekCommand(sublime_plugin.ApplicationCommand):

	def run(self):
		now = datetime.datetime.today()
		first = now - datetime.timedelta(now.weekday())
		last = now + datetime.timedelta(6 - now.weekday())

		s = "Week %s is from %s until (and including) %s." % (now.strftime("%W"), first.strftime("%A %B %d, %Y"), last.strftime("%A %B %d, %Y"))
		sublime.message_dialog(s)