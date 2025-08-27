import document
import md_writer


hugo_strategy = document.Strategy(  ".md",
                                    md_writer.make_ref_for_header, 
                                    md_writer.make_ref_for_text, 
                                    md_writer.resolve_refs_conflict,
                                    md_writer.process_internal_link)